# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pylab as plt
import tables
from icecube.weighting import weighting
from icecube.weighting import fluxes as flx
import h5py
import time


# In[2]:

from optparse import OptionParser
import sys, os, glob


# In[3]:

def MakeWeightList(SelectStr=None):
    All = []
    All.append(('GaisserH3a','gh3a',flx.GaisserH3a()))
    All.append(('GaisserH4a','gh4a',flx.GaisserH4a()))
    All.append(('GaisserHillas','ghill',flx.GaisserHillas()))
    All.append(('Glasstetter','glas',flx.Glasstetter()))
    All.append(('Hoerandel5','hoer5',flx.Hoerandel5()))
    All.append(('Hoerandel','hoer1',flx.Hoerandel()))
    
    strAll = ''
    if SelectStr is None:
        for Name,Short,Func in All:
            strAll += Short + '-'
        return strAll+'poly'
    
    RetList = []
    for Name,Short,Func in All:
        if Short in SelectStr:
            RetList.append((Name,Short,Func))
    return RetList


def Infoprint(filename,dataset,nfiles):
    print '\nReweighting: '
    print '\t Filename:\t'+filename
    print '\t Dataset:\t'+str(dataset)
    print '\t NFiles:\t'+str(nfiles)

def main():
    ListOfModels = MakeWeightList()
    parser = OptionParser()
    parser.add_option("-I", "--infile", dest="infile",default=None)
    parser.add_option("-O", "--outfile", dest="outfile",default=None)
    parser.add_option("-D", "--dataset", dest="dataset",default=None)
    parser.add_option("-M", "--models", dest="models",help='default: '+ListOfModels,default=ListOfModels)

    (options, args) = parser.parse_args()
    options.dataset = int(options.dataset)
    if options.infile is None:
        print 'No infile given!'
        sys.exit(1)
    if options.dataset is None:
        print 'No dataset given!'
        sys.exit(1)
    
    if options.outfile is None:
        options.outfile = np.str(options.infile).replace('.hd5','_Weights.hd5')

    #print options.infile, options.outfile
    
    ChosenList = MakeWeightList(options.models)
    InFile = tables.openFile(options.infile)
    
    
    Run = InFile.root.MCPrimary1.cols.Run[:]
    Event = InFile.root.MCPrimary1.cols.Event[:]
    SubEvent = InFile.root.MCPrimary1.cols.SubEvent[:]
    energy = InFile.root.MCPrimary1.cols.energy[:]
    ptype = InFile.root.MCPrimary1.cols.type[:]
    
    WMAPtimescale = InFile.root.CorsikaWeightMap.cols.TimeScale[:]
    WMAPweight = InFile.root.CorsikaWeightMap.cols.Weight[:]
    WMAPpolygonato = InFile.root.CorsikaWeightMap.cols.Polygonato[:]
    WMAPDiplopia= InFile.root.CorsikaWeightMap.cols.DiplopiaWeight[:]
    
    nfiles, generator = weighting.from_simprod(options.dataset)
    if options.dataset == 10309:
        nfiles = 14346
    generator = nfiles*generator
    genvalues = generator(energy,ptype)
    
    Infoprint(options.infile,options.dataset,nfiles)
    
    GrpName = 'U_Weights'
    FinalTableLayout = [('Run', Run.dtype)
                                                      ,('Event',Event.dtype)
                                                      ,('SubEvent', SubEvent.dtype)
                                                      ,('Energy',energy.dtype)
                                                      ,('ParticleType', ptype.dtype)
                                                      ,('GenValues', genvalues.dtype)
                                                      ,('TimeScale', WMAPtimescale.dtype)
                                                      ]
    
    for Name,Short,Func in ChosenList:
        FinalTableLayout.append((Name,'<f8'))
    if 'poly' in options.models:
        FinalTableLayout.append(('Polygonato','<f8'))
        
    Data = np.zeros((len(Run),), dtype=FinalTableLayout)
    Data['Run']=Run
    Data['Event']=Event
    Data['SubEvent']=SubEvent
    Data['Energy']=energy
    Data['ParticleType']=ptype
    Data['GenValues']=genvalues
    Data['TimeScale']=WMAPtimescale
    
    #print Data['Run']
    for Name,Short,Func in ChosenList:
        Data[Name]=Func(energy,ptype)/(genvalues)
    
    if 'poly' in options.models:
        Data['Polygonato'] = WMAPweight*WMAPpolygonato*WMAPDiplopia/(WMAPtimescale*nfiles)
    
    OutFile = tables.openFile(options.outfile,'w')    
    A = OutFile.createTable('/','U_Weights',Data)
    
    OutFile.close()
    InFile.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
