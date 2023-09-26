#!/usr/bin/env python

import os
from I3Tray import *
from os.path import *
import sys

from icecube import tableio
from icecube.tableio import I3TableWriter
from icecube import icetray, dataclasses, dataio, WaveCalibrator
from icecube.icetray import I3Units
# from icecube import SeededRTCleaning
from icecube import STTools
icetray.load('wavedeform', False)


@icetray.traysegment
def CalibrationAndCleaning(tray, name):

    def CheckRawData(frame):
        if frame.Has('InIceRawData'):
            return True
        return False

    tray.AddModule(CheckRawData,
                   'check-raw-data',
                   Streams=[icetray.I3Frame.Physics])

    tray.AddModule('I3WaveCalibrator',
                   'calibrator')(
        ('Launches', 'InIceRawData'),
        ('Waveforms', 'CalibratedWaveforms'),
        ('ATWDSaturationMargin', 123),
        ('FADCSaturationMargin', 0),
        ('Errata', 'OfflineInIceCalibrationErratas'),
        ('WaveformRange', 'CalibratedWaveformRanges')
    )

    tray.AddModule('I3WaveformSplitter', 'waveformsplit')(
        ('Input', 'CalibratedWaveforms'),
        ('HLC_ATWD', 'CalibratedWaveformsHLCATWD'),
        ('HLC_FADC', 'CalibratedWaveformsHLCFADC'),
        ('SLC', 'CalibratedWaveformsSLC'),
        ('Force', True),
    )

    # Prep for SRT cleaning
    tray.AddModule('I3Wavedeform', 'pulse-extraction')(
        ('OutPut', 'OfflinePulses'),
        ('WaveformTimeRange', 'CalibratedWaveformRange'),
        ('Waveforms', 'CalibratedWaveforms'),
        ('If', lambda frame: not frame.Has('SRTOfflinePulses')),
    )

    # # SeededRT cleaning on RecoPulses
    # tray.AddModule('I3SeededRTHitCleaningModule<I3RecoPulse>',
    #                'SeededRTCut')(
    #     ('InputResponse', 'OfflinePulses'),
    #     ('OutputResponse', 'SRTOfflinePulses'),  # Name of output Launches
    #     ('RTRadius', 150),  # Radius for RT cleaning
    #     ('RTTime', 1000),  # Time for RT cleaning
    #     ('DeepCoreRTRadius', -1),  # Default
    #     ('DeepCoreRTTime', -1),  # Default
    #     ('MaxIterations', 3),  # Default
    #     ('Seeds', 'HLCcore'),  # Default
    #     ('HLCCoreThreshold', 2),  # Default
    #     ('CylinderHeight', -1),  # Default
    #     ('If', lambda frame: not frame.Has('SRTOfflinePulses')),
    # )

    # SRT cleaning from STTools since seededRTCleaning module is deprecated
    from icecube.STTools.seededRT.configuration_services \
        import I3DOMLinkSeededRTConfigurationService
    stConfigService = I3DOMLinkSeededRTConfigurationService(
        allowSelfCoincidence=False,
        useDustlayerCorrection=True,
        dustlayerUpperZBoundary=0*I3Units.m,
        dustlayerLowerZBoundary=-150*I3Units.m,
        ic_ic_RTTime=1000*I3Units.ns,
        ic_ic_RTRadius=150*I3Units.m
    )

    tray.AddModule('I3SeededRTCleaning_RecoPulse_Module',
                   'STTools_SRTCleaning',
                   InputHitSeriesMapName='OfflinePulses',
                   OutputHitSeriesMapName='SRTOfflinePulses',
                   stConfigService=stConfigService,
                   SeedProcedure='HLCCoreHits',
                   NHitsThreshold=2,
                   If=lambda frame: not frame.Has('SRTOfflinePulses'))

    return

##################
# Testing
##################
if __name__ == '__main__':
    #################
    # IC86-II
    #################
    print('Testing for NuTau IC86-II:')
    outputfile = '/data/user/mmeier/tests/test_waveform_calib.i3.bz2'
    inputfile = '/data/sim/IceCube/2012/filtered/level2/' + \
        'neutrino-generator/11065/00000-00999/' + \
        'Level2_IC86.2012_nugen_NuTau.011065.000001.i3.bz2'
    gcdfile = '/data/sim/IceCube/2012/filtered/level2/neutrino-generator/' + \
        '11065/01000-01999/GeoCalibDetectorStatus_2012.56063_V1.i3.gz'

    tray = I3Tray()
    tray.AddModule('I3Reader', 'reader', Filenamelist=[gcdfile, inputfile])

    tray.AddSegment(CalibrationAndCleaning, 'CalibAndCleaning')

    tray.AddModule('I3Writer', 'writerI3', FileName=outputfile,
                   Streams=[icetray.I3Frame.Physics, icetray.I3Frame.DAQ])

    tray.AddModule('TrashCan', 'YesWeCan')
    tray.Execute(100)
    tray.Finish()
