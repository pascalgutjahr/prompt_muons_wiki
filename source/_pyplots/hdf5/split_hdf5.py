#!/usr/bin/env python
# coding: utf-8

import numpy as np
import h5py
import sys, os, glob, getopt

def main(argv):
    inputfile = ''
    parts = 0
    try:
        opts, args = getopt.getopt(argv,"hi:p:",["input=","parts="])
    except getopt.GetoptError:
        print 'splitt_hdf5.py -i <inputfile> -p <parts>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'splitt_hdf5.py -i <inputfile> -p <parts>'
            sys.exit()
        elif opt in ("-i", "--intput"):
            inputfile = arg
        elif opt in ("-p", "--parts"):
            parts = int(arg)
    print 'Input file is "', inputfile
    print 'Number of parts is "', parts

    # load original file
    original = h5py.File(inputfile, "r")
    
    for part in range(1, parts + 1):
    	outputfile = inputfile[:-4] + '_' + str(part) + '.hd5'
        newfile = h5py.File(outputfile, 'a')

        for attr in original:
            oldlength = original[attr].shape[0]
            newlength = int(oldlength / parts)
            start = (part - 1) * newlength
            stop = part * newlength

            # make sure last part has right length
            if part == parts:
                stop = oldlength

        	
            dset = newfile.create_dataset(attr, data=original[attr][start:stop])
        	newfile.flush()
        newfile.close()

if __name__ == "__main__":
   main(sys.argv[1:])
