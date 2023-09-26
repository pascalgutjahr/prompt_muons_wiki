#!/usr/bin/python
# coding: utf-8

from functools import reduce
from hdfchain import HDFChain

def loadData(paths):
    '''
        Load hdf5 files and generate list of all shared attributes. Multiple
        files per dataset are allowed and handed as one file using hdfchain.

        Args:
            paths: expects a dictionary with lists of paths to hdf5 files

        Returns:
            A dictionary with loaded data sets, list of all shared attributes
    '''
    data = {}
    all_attributes = []
    for dataset, path in paths.items():
        data[dataset] = HDFChain(path)
        all_attributes.append(data[dataset]._tables.keys())

    attributes = reduce(set.intersection, map(set, all_attributes))

    return data, attributes

