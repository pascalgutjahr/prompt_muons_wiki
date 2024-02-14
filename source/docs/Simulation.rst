New CORSIKA extended history simulations
########################################

New CORSIKA datasets are simulated and stored at: 

* /data/sim/IceCube/2023/generated/CORSIKA_EHISTORY/

The simulation is divided into 4 different energy ranges. Since the simulation is done out ourselves, the dataset numbers are not provided in iceprod.

* 30010: 600 GeV - 1 PeV

* 30011: 1 PeV - 100 PeV

* 30012: 100 PeV - 1 EeV

* 30013: 1 EeV - 50 EeV

The following settings are used:

* CORSIKA version 77420 

* SIBYLL 2.3d 

* Icetray 1.5.1

* 5 components (p, He, N, Al, Fe)

* Component norm: [10, 5, 3, 2, 1]

* Zenith angle: 0 - 90 degrees

* Polyplopia: True 

* Ecuts1: 273 GeV (hadron min energy)

* Ecuts2: 273 GeV (muon min energy)

* Ecuts3: 1020 GeV (electron min energy)

* Ecuts4: 1020 GeV (photon min energy)

* TrimShower: True 

* Atmosphere: ``ratmo: 4`` (April) 

* Spectrum : -1 (increase high energy statistics)

This simulation is performed to test the extended history and prompt tagging software. Thus, the statistics are not yet sufficient.
The built CORSIKA software is stored at: ``/data/user/pgutjahr/software/CORSIKA/corsika-77420/bin/`` and also available in the cvmfs:
``/cvmfs/icecube.opensciencegrid.org/users/pgutjahr/software/CORSIKA/``

Verification
++++++++++++

* WHAT EXACTLY HAVE WE DONE TO VERIFY OUR SIMULATIONS?

* WHAT NEEDS TO BE DONE TO VERIFY IT?

Dataset exploration - Level 2
+++++++++++++++++++++++++++++
In the following, unweighted distributions of the simulated events are shown. In :numref:`simulated_events_primary_energy`, the primary distribution are shown 
for each dataset.

.. _simulated_events_primary_energy:
.. figure:: images/plots/dataset_exploration/simulated_events_primary_energy.pdf 

    : The energy distribution of primary particles is shown for the four different simulation datasets.

In :numref:`simulated_events_5_components_primary_energy`, the primary distributions are shown for each dataset, separated by the primary particle type.

.. _simulated_events_5_components_primary_energy: 
.. figure:: images/plots/dataset_exploration/simulated_events_5_components_primary_energy.pdf

    : The energy distribution of primary particles is shown for the four different simulation datasets, separated by the primary particle type.

In :numref:`simulated_events_leading_muon_energy`, the energy distribution of the leading muon is shown for each dataset. The leading muon is defined 
as the muon with the highest energy in the muon bundle. The shown energy corresponds to the energy at the detector entry.

.. _simulated_events_leading_muon_energy:
.. figure:: images/plots/dataset_exploration/simulated_events_leading_muon_energy.pdf

    : The energy distribution of the leading muon is shown for the four different simulation datasets.
    
In :numref:`simulated_events_bundle_muon_energy`, the energy distribution of the muon bundle is shown for each dataset. The muon bundle is defined as the
the sum of the energy of all muons entering the detector.

.. _simulated_events_bundle_muon_energy:
.. figure:: images/plots/dataset_exploration/simulated_events_bundle_muon_energy.pdf

    : The energy distribution of the muon bundle is shown for the four different simulation datasets.
    

Estimation of the simulated statistics
++++++++++++++++++++++++++++++++++++++

The estimation of the simulated statistics needed for this analysis is not easy to determine. The statistics should be sufficient in the 
phase space of the analysis. This will probably be defined by the zenith angle of the incoming muon and the muon energy. Here, 
both the leading and bundle energy at detector entry and at the surface are considered. Furthermore, the systematic uncertainties in this 
phase space need to be known to create a simulation with statistical uncertainties lower than the systematic uncertainties.
However, to get a first impression of the statistics simulated so far, :numref:`energy_spectrum_primary_energy_simulation_muonfilter_bundle_cut_1e5` 
and :numref:`energy_spectrum_leading_muon_energy_simulation_muonfilter_bundle_cut_1e5` show the energy spectrum of the primary and leading muon energy. The 
simulated events are shown in blue, in orange the events are weighted to the expected statistics of 1 year of IceCube data using GlobalSplineFit5Comp (GSF) 
weightig. Here, the muon filter is applied and an energy cut of 100 TeV is applied to the muon bundle energy at the detector entry. For leading muon energies 
above 500 TeV, more muons are simulated than expected for 1 year. (The cuts applied here are not the final cuts for the analysis, but the cuts used for the pseudo 
analysis.)

.. _energy_spectrum_primary_energy_simulation_muonfilter_bundle_cut_1e5:
.. figure:: images/plots/toy_analysis_1year/energy_spectrum_primary_energy_simulation_muonfilter_bundle_cut_1e5.pdf

    : Primary energy spectrum is shown to estimate the simulated statistics.
    
.. _energy_spectrum_leading_muon_energy_simulation_muonfilter_bundle_cut_1e5:
.. figure:: images/plots/toy_analysis_1year/energy_spectrum_leading_muon_energy_simulation_muonfilter_bundle_cut_1e5.pdf
    
    : Leading muon energy spectrum is shown to estimate the simulated statistics.

 
Large scale simulation 
++++++++++++++++++++++
The large scale simulation with sufficient statistics will be performed with Iceprod and provided as an official dataset. 
To start this simulation, the following questions need to be answered:

* Does cutting of the electromagnetic shower component have any impact on our phase space (high energy muons)? This is done by `Ecuts3` and `Ecuts4`.
    - 10% effect possible on the muon energy spectrum, but no significant effect on the runtime and disc space -> EM component will be turned on

* Shall we stay with Icetray 1.5.1? Were any bugs fixed in the latest versions? 
    - Use latest version of Icetray to include any possible bug fixes and up-to-date software + latest ice model

* We haven't oversampled our showers yet. Which factor for oversampling is usual? 
    - At low energies, oversampling up to 10 is common, but this should be decreased at higher energies. 
    - Not yet decided! 

* How can we reduce the disc space?
    - For the final simulation, we will store step 0 and level 2 files. The extended I3MCTrees can be removed, since we can re-simulate them using PROPOSAL if needed.

* How much disk storage do we need for the final simulation? 
    - Not clear yet!

* Which seasons do we want to simulate? 4 seasons?
    - We want to simulate all 12 seasons as defined `here <https://wiki.icecube.wisc.edu/index.php/Real_atmosphere_for_CORSIKA>`_, 
    matched by the run number. This enables further studies of the seasonal variations in the future.

* Do we want to set the TrimShower option?
    - For large zenith angles, even high energy muon can be cut off. For the calculation of the effective area, we have to turn off trimshower
    - Not yet decided!