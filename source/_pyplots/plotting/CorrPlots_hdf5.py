
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pylab as plt
import matplotlib as mpl
from matplotlib.backends.backend_pdf import PdfPages
import tables
import matplotlib.gridspec as gridspec
import imp
from optparse import OptionParser
import warnings
from optparse import OptionParser
import warnings
import os
import sys

def StrToBool(S):
    if S=='1' or S=='True' or S=='true' or S=='t':
        return True
    else:
        return False

def GetGrpValFromPath(SS):
    return [SS[:SS.rfind('/')], SS[SS.rfind('/')+1:]]

def GetDataFromLine(Line):
    Line1 = Line.strip().split()
    return {'PathX': GetGrpValFromPath(Line1[0]),
            'NameX': str(Line1[1]),
            'PathY': GetGrpValFromPath(Line1[2]),
            'NameY': str(Line1[3]),
            'LogX': StrToBool(Line1[4]),
            'LogY': StrToBool(Line1[5]),
            'LogZ': StrToBool(Line1[6]),
            'CMin': float(Line1[7])}


def Make2dHist(DataX=None,DataY=None,NBins=201,Mask=None,LogX=False,LogY=False,LogZ=False,NameX='X',NameY='Y',Weights=None,CMin=.1):
    #Create Mask
    if Mask==None:
        Mask=np.ones(len(DataX),dtype=bool)
    
    #Create Weights
    if Weights==None:
        Weights=np.ones(len(DataX),dtype=bool)
    
    #Apply LogX Option
    if LogX:
        DataX = np.log10(DataX[Mask])
        NameX = 'log10(' + NameX +')'
    else:
        DataX = DataX[Mask]
    
    #Apply LogY Option
    if LogY:
        DataY = np.log10(DataY[Mask])
        NameY = 'log10(' + NameY +')'
    else:
        DataY = DataY[Mask]
    
    #Apply LogZ Option
    if LogZ:
        _norm = mpl.colors.LogNorm()
    else:
        _norm = mpl.colors.Normalize()
    
    #Plot
    plt.hist2d(DataX,
               DataY,
               bins=NBins,
               norm=_norm,
               weights=Weights,
               cmin=CMin)
    plt.xlabel(NameX)
    plt.ylabel(NameY)
    plt.colorbar()

def PrintOptions(OPT):
    print 'Options:'
    print '\tDatafile:',OPT.datafile
    print '\tComparetxt:',OPT.comparetxt
    print '\tWeights:',OPT.weights
    print '\tNormalizeweights:',OPT.normalizeweights
    print '\tOutput path:',OPT.outpath
    print '\tAppendix:',OPT.appendix
    print '\tVerbose:',OPT.verbose
    
    

def main():
    Usage = 'python CorrPlots_hdf5.py --datafile /home/tfuchs/Phd/Data/10668_10809_L4_20k_60k_Test_Labeled.hd5 \
    --comparetxt CorrPlots_hdf5.txt \
    --weights=/data/UH3a_Weight_Norm \
    --normalizeweights 1000000 \
    --outpath /home/tfuchs/data_tmp \
    --appendix AllesMist- \
    --verbose'
    parser = OptionParser(usage=Usage)
    
    parser.add_option("-D", "--datafile", dest="datafile",default=None,help='Data file to plot the comparisons for.')
    parser.add_option("-C", "--comparetxt", dest="comparetxt",default=None,help='Steering file for the script with attributes, names and scalings.')
    
    parser.add_option("-W", "--weights", dest="weights",default=None,help='Where to find the weights for the events. Else everything is weight 1.')
    parser.add_option("-N", "--normalizeweights", dest="normalizeweights",type=float,default=-1,help='Renormalize the weights to a certain total number.')
    
    parser.add_option("-P", "--outpath", dest="outpath",default="",help='Output path for the created plots.')
    parser.add_option("-A", "--appendix", dest="appendix",default="",help='Appendix for all plots to set before the comparison names.')
    
    parser.add_option("-V", "--verbose",action="store_true",default=False,help='Enable more output.')
    
    (options, args) = parser.parse_args()
    
    #Check output path
    #############################################
    if not options.outpath.endswith('/'):
        options.outpath = options.outpath+'/'
    if not os.path.exists(options.outpath):
        print '!!! Path ('+options.outpath+') does not exist! Creating...'
        os.mkdir(options.outpath)
    #############################################
    
    PrintOptions(options)
    
    if options.datafile is None or options.comparetxt is None:
        print 'Datafile and CompareTxt has to be defined!!!'
        print 'Use --help option for usage'
        sys.exit(0)
        
    TestFile = tables.openFile(options.datafile)
    
    #Modify Weights
    #############################################
    Weights = None
    if options.weights is not None:
        tmp_path, tmp_val = GetGrpValFromPath(options.weights)
        Weights = TestFile.get_node(where=tmp_path).col(tmp_val)[:]
        if options.normalizeweights > 0:
            Weights = Weights* options.normalizeweights / sum(Weights)
        if options.verbose:
            print 'Weights from:',tmp_path,tmp_val
            print 'Weights[:10]:',Weights[:10]
            print ''
    #############################################
    
    CompareFile = file(options.comparetxt,'r')
    
    TmpLine = '###'
    while TmpLine != '':
        #Get Line and check if it should not be ignored
        #############################################
        TmpLine = CompareFile.readline()
        if TmpLine=='' or TmpLine[0]=='#':
            continue
        data = GetDataFromLine(TmpLine)
        #############################################
        if options.verbose:
            print TmpLine
        
        Make2dHist(DataX = TestFile.get_node(where=data['PathX'][0]).col(data['PathX'][1])[:],
               DataY = TestFile.get_node(where=data['PathY'][0]).col(data['PathY'][1])[:],
               NameX = data['NameX'],
               LogX = data['LogX'],
               NameY = data['NameY'],
               LogY = data['LogY'],
               LogZ = data['LogZ'],
               CMin = data['CMin'],
               Weights=Weights)
        plt.savefig(options.outpath +
                    options.appendix +
                    data['NameX']+'_vs_'+ data['NameY']+
                    '.png')
        plt.clf()
    CompareFile.close()
    TestFile.close()

if __name__ == "__main__":
    main()


