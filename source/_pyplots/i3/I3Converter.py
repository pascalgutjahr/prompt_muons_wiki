#!/usr/bin/env python
# coding: utf-8

from I3Tray import *
import sys, os, glob, getopt, errno
import copy
from optparse import OptionParser
from icecube.tableio import I3TableWriter, I3CSVTableService
from icecube.hdfwriter import I3HDFTableService
from icecube.rootwriter import I3ROOTTableService
from icecube import icetray, dataclasses, dataio, simclasses, phys_services
from icecube import common_variables

NewEventID=0

def main(argv):
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="inputpath",
                      help="Inputpath to crawl for files.")
    parser.add_option("-o", "--output", dest="outputfile",
                      help="Outputfile")
    parser.add_option("-f", "--format", dest="format", default="hd5",
                      help="Choose outputformat. Available hd5 and root.")
    parser.add_option("-p", "--primary", dest="primary", default=False,
                      action="store_true",
                      help="Define if 'I3MCPrimary' should be created.")
    parser.add_option("-I", "--ID", dest="generateID", default=False,
                      action="store_true",
                      help="Generate new p-frame-based ID.")
    (options, args) = parser.parse_args()


    print 'Input folder is "', options.inputpath
    print 'Output file is "', options.outputfile
    print 'Outputformat is "', options.format
    if options.primary:
        print 'I3MCPrimary will be created.'
    if options.generateID:
        print 'P-frame-based ID will be added to "I3EventHeader".'

    i3_ending = '.i3.bz2'

    # create list of all files of input path
    i3_files = []
    print("Filenames:")
    for filename in os.listdir(inputpath):
        print filename
        if i3_ending in filename or i3_ending[:-4] in filename:
            i3_files.append(inputpath + filename)
    print i3_files

    tray = I3Tray()
    tray.AddModule('I3Reader', 'reader', FilenameList = i3_files)

    # create output path if necessary
    if not os.path.isdir(os.dirname(out_file)):
        os.makedirs(os.dirname(out_file))

    # choose output format
    if format == "root":
        service = I3ROOTTableService(outputfile + '.root', 'master_tree')
        print('Storing in ' + outputfile + '.root')
    elif format == "hd5":
        service = I3HDFTableService(outputfile + '.hd5')
        print('Storing in ' + outputfile + '.hd5')
    else:
        print 'Using standard format: hd5.'
        service = I3HDFTableService(outputfile + '.hd5')
        print('Storing in ' + outputfile + '.hd5')

    if options.primary:
        # create extra attribute for primary energy
        def SaveMCPrimary(frame):
            frame['I3MCPrimary']=frame['I3MCTree'].primaries[0]
        tray.AddModule(SaveMCPrimary,'SavePrimary')


    def ModifyHeader(frame):
        global NewEventID
        header = copy.copy(frame['I3EventHeader'])
        del frame['I3EventHeader']
        header.run_id = NewEventID
        NewEventID = NewEventID + 1
        frame['I3EventHeader'] = header

    if options.generateID:
        tray.AddModule(ModifyHeader, 'HeaderModifier')

    # write chosen attributes
    tray.AddModule(I3TableWriter,'writer',
                   tableservice = [service],
                   BookEverything = True,
                   SubEventStreams = ['in_ice']
                  )

    # close file
    tray.AddModule('TrashCan','can')
    tray.Execute()
    tray.Finish()


if __name__ == "__main__":
   main(sys.argv[1:])
