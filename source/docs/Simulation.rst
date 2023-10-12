New CORSIKA extended history simulations
########################################

New CORSIKA datasets are simulated and stored at: 

* /data/sim/IceCube/2023/generated/CORSIKA_EHISTORY/

The simulation is divided into 4 different energy ranges. The dataset numbers are not provided in iceprod:

* 30010: 600 GeV - 1 PeV

* 30011: 1 PeV - 100 PeV

* 30012: 100 PeV - 1 EeV

* 30013: 1 EeV - 50 EeV

The following settings are used:

* CORSIKA version 77420 

* SIBYLL 2.3d 

* Icetray 1.5.1

* 5 components (p, He, N, Al, Fe)

* Polyplopia: True 

* Ecuts1: 273 GeV (hadron min energy)

* Ecuts2: 273 GeV (muon min energy)

* Ecuts3: 1020 GeV (electron min energy)

* Ecuts4: 1020 GeV (photon min energy)

This simulation is performed to test the extended history and prompt tagging software. Thus, the statistics are not yet sufficient.

Verification
++++++++++++

* WHAT EXACTLY HAVE WE DONE TO VERIFY OUR SIMULATIONS?

* WHAT NEEDS TO BE DONE TO VERIFY IT?

Estimation of the simulated statistics
++++++++++++++++++++++++++++++++++++++
.. image:: images/plots/dataset_exploration/simulated_events_primary_energy.pdf 
    :width: 49%

.. image:: images/plots/dataset_exploration/simulated_events_5_components_primary_energy.pdf
    :width: 49%

.. image:: images/plots/dataset_exploration/simulated_events_leading_muon_energy.pdf
    :width: 49%

.. image:: images/plots/dataset_exploration/simulated_events_bundle_muon_energy.pdf
    :width: 49%

.. figure:: images/plots/data_mc/effective_livetime.pdf

.. image:: images/plots/toy_analysis_1year/energy_spectrum _primary_energy_simulation_muonfilter_bundle_cut_1e5.pdf
    :width: 49%

.. image:: images/plots/toy_analysis_1year/energy_spectrum_leading_muon_energy_simulation_muonfilter_bundle_cut_1e5.pdf
    :width: 49%


 
Large scale simulation 
++++++++++++++++++++++
The large scale simulation with sufficient statistics will be performed with Iceprod and provided as an official dataset. 
To start this simulation, the following questions need to be answered:

* Does cutting of the electromagnetic shower component have any impact on our phase space (high energy muons)? This is done by `Ecuts3` and `Ecuts4`.

* Shall we stay with Icetray 1.5.1? Were any bugs fixed in the latest versions? 

* We haven't oversampled our showers yet. Which factor for oversampling is usual? 

* How much disk storage do we need for the final simulation? 

