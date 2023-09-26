"""
A proxy that mimicks some of the tables.File API to allow multiple
discrete files to be read as a single object.

(c) 2009-ish Eike Middell <middell@ifh.de>
"""

import numpy as n
import tables
from glob import glob
from collections import defaultdict
from logging import getLogger

class HDFTableProxy(object):
	def __init__(self, table, files):
		self.path = str(table._v_pathname)
		self._v_dtype = table.description._v_dtype
		self.attrs = table.attrs
		self.description = table.description
		self.files = files
	
	@property
	def colnames(self):
		return self._v_dtype.names
	
	@property
	def nrows(self):
		return self.lengths.sum()
		
	@property
	def lengths(self):
		if hasattr(self, "_lengths"):
			return self._lengths
		self._lengths = n.zeros(len(self.files), dtype=int)
		# first loop to calculate number of rows
		for i, file in enumerate(self.files):
			try:
				self._lengths[i] = len(file.getNode(self.path))
			except tables.NoSuchNodeError:
				getLogger("cubicle.hdfchain.HDFTableProxy").warn("node %s does not exist in file %s", self.path, file.filename)
				# print "WARN: node %s does not exist in file %s" % (self.path, file.filename)
				self._lengths[i] = 0
		return self._lengths

	def read(self, field=None):
		
		if field is not None:
			return self.col(field)

		# create result array ...
		lengths = self.lengths
		result = n.zeros(lengths.sum(), dtype=self._v_dtype)
		
		# .. and fill it
		for i, file in enumerate(self.files):
			if lengths[i] == 0:
				continue
			result[lengths[:i].sum():lengths[:i].sum()+lengths[i]] = file.getNode(self.path).read()

		return result

	def read_iter(self):
		for i, file in enumerate(self.files):
			yield file.getNode(self.path).read()
	
	def col_iter(self, colname):
		for i, file in enumerate(self.files):
			yield file.getNode(self.path).col(colname)

	def col(self, colname):
		
		# first loop to calculate number of rows and pick up the datatype
		lengths = n.zeros(len(self.files), dtype=int)
		#print "INFO: counting rows"
		dtype = None
		for i, file in enumerate(self.files):
			try:
				node = file.getNode(self.path)
				lengths[i] = len(node)
				if dtype is None:
					try:
						dtype = node._v_dtype[colname]
					except KeyError:
						pass
			except tables.NoSuchNodeError:
				getLogger("cubicle.hdfchain.HDFTableProxy").warn("node %s does not exist in file %s", self.path, file.filename)
				# print "WARN: node %s does not exist in file %s" % (self.path, file.filename)
				lengths[i] = 0
		
		if dtype is None:
			raise KeyError('Field %s/%s not found' % (self.path, colname))

		# create result array ...
		result = n.zeros(lengths.sum(), dtype=dtype)
		
		# .. and fill it
		for i, file in enumerate(self.files):
			getLogger("cubicle.hdfchain.HDFTableProxy").debug("read %d/%d", i+1, len(self.files))
			if lengths[i] == 0:
				continue
			try:
				col = file.getNode(self.path).col(colname)
			except KeyError:
				getLogger("cubicle.hdfchain.HDFTableProxy").warn("field %s/%s does not exist in file %s. Filling with NaN.", self.path, colname, file.filename)
				# print "WARN: field %s/%s does not exist in file %s. Filling with NaN." % (self.path, colname, file.filename)
				col = n.nan
			result[lengths[:i].sum():lengths[:i].sum()+lengths[i]] = col

		return result

	def __len__(self):
		length = 0
		for i, file in enumerate(self.files):
			length += len(file.getNode(self.path))
		return length

	def __repr__(self):
		return ("chained table with %d files:\n" % len(self.files))+self.files[0].getNode(self.path).__repr__()

class TableAccessor(object):
	"""
	Mimick the root group of tables.File
	"""
	def __init__(self, tabledict):
		self._v_children = tabledict
		for tabname, proxy in tabledict.iteritems():
			self.__dict__[tabname] = proxy

	def __repr__(self):
		return ", ".join([key for (key,value) in self.__dict__.iteritems() if type(value) is HDFTableProxy])

class HDFChain(object):
	def __init__(self, files, maxdepth=1, verbose=False, **kwargs):
		""" 
		setup a chain of hdf files. 
		files is either a list of filenames or a glob string
		kwargs are passed to tables.openFile (e.g. NODE_CACHE_SLOTS)
		"""
		
		self.files = list()
		self._tables = defaultdict(HDFTableProxy)
		self.verbose = verbose
		self.pathes = dict()

		if self.verbose:
			print "opening files in chain..."
		if type(files) is list:
			if len(files) == 0:
				raise ValueError("Need at least 1 file to make a chain")
			self._open_files(files, **kwargs)
		elif type(files) is str:
			filelist = sorted(glob(files))
			if len(files) == 0:
				raise ValueError("The globstring '%s' does not match any files" % files)
			self._open_files(filelist, **kwargs)
		else:
			raise ValueError("parameter files must be either a list of filenames or a globstring")
		
		if len(self.files) == 0:
			raise IOError("No valid files found!")

		file = self.files[0]
		if self.verbose:
			print "walking through first file %s" % file.filename
		for table in file.walkNodes(classname="Table"):
			if table._v_depth > maxdepth:
				continue
			if table.name in self._tables:
				getLogger("cubicle.hdfchain.HDFChain").warn("skipping additional occurence of table %s at %s (using %s)!", table.name, 
					  table._v_pathname, self._tables[table.name].path)
				# print "WARN: skipping additional occurence of table %s at %s (using %s)!" % (table.name, 
				# 	  table._v_pathname, self._tables[table.name].path)
				continue
			else:
				proxy = HDFTableProxy(table, self.files)
				self._tables[table.name] = proxy
				self.pathes[table._v_pathname] = proxy
			
		self.root = TableAccessor(self._tables)

	def _open_files(self, paths, **kwargs):
		self.files = list()
		for path in paths:
			try:
				hdf = tables.openFile(path, **kwargs)
				self.files.append(hdf)
			except tables.HDF5ExtError:
				getLogger("cubicle.hdfchain.HDFChain").error("'%s' is corrupt! Skipping...", path)

	def close(self):
		for tabname, tabproxy in self._tables.iteritems():
			tabproxy.file = None
		self._tables.clear()
		
		while len(self.files) > 0:
			self.files.pop().close()
			
	def __del__(self):
		self.close()

	def getNode(self, path):
		if path in self.pathes:
			return self.pathes[path]
		else:
			raise tables.NoSuchNodeError(path)
		
