New CORSIKA extended history simulations
########################################

New CORSIKA datasets are simulated and stored at: 

* /data/sim/IceCube/2023/generated/CORSIKA_EHISTORY/

At first, in 2023 test simulations were performed using the software `simulation_scripts <https://github.com/tudo-astroparticlephysics/simulation_scripts>`_. 
This software is a framework similar to IceProd, but it is used for local simulations on our Madison cluster. It imports all the icetray functions that are used in 
any other IceCube simulation. The main difference is that this framework is maintained locally in Dortmund and thus it's easier to adapt to our needs.

The test datasets are named ``30010``, ``30011``, ``30012`` and ``30013``. Caution, these numbers do **not** correspond to the official dataset numbers.
We used these simulations to develop and test this analysis of the prompt component of the atmospheric muon flux. 
First dataset explorations are stored in :ref:`Appendix/First extended history simulations <first extended history simulations paragraph>`. 


For the official analysis, we will provide 
an official dataset simulated with IceProd to make it re-producible for the entire IceCube community.
    
 
Official CORSIKA Ehist IceProd simulation 
+++++++++++++++++++++++++++++++++++++++++

----

*Note*: In the icetray version 1.11.0-rc1, a bug was introduced that we fixed locally without committing to move on 
with our simulation to perform further tests. Hence, this is still a preliminary simulation since we want to provide 
a simulation that is re-producible (using an official icetray version tag).

----

A preliminary large-scale simulation is currently performed with Iceprod. 
The datasets are:

* 22774: 1e4 GeV - 1e6 GeV 
* 22775: 1e6 GeV - 1e8 GeV
* 22776: 1e8 GeV - 1e9 GeV
* 22777: 1e9 GeV - 1e10 GeV
* 22778: 1e10 GeV - 1e11 GeV

The following settings are used:

* CORSIKA version 77500 

* SIBYLL 2.3d 

* Icetray 1.11.0-rc1

* 5 components (p, He, N, Al, Fe)

* Zenith angle: 0 - 90 degrees

* Polyplopia: False (no coincident events are simulated)

* Ecuts1: 273 GeV (hadron min energy)

* Ecuts2: 273 GeV (muon min energy)

* Ecuts3: 273 GeV (electron min energy)

* Ecuts4: 273 GeV (photon min energy)

* TrimShower: False 

* Atmosphere: all 12 seasons (defined `here <https://wiki.icecube.wisc.edu/index.php/Real_atmosphere_for_CORSIKA>`_)

The detailed settings can be found in the config files at `IceProd <https://iceprod2.icecube.wisc.edu>`_


---- 

In the following two figures, the primary energy distribution of the simulated CORSIKA Ehist IceProd datasets is shown on level 2 
for the different primary particles. No cuts or filters are applied. This is not the entire statistics, but a subset of the data.
The relative ratios of the primaries are different for each dataset to match the contributions of the 
primaries to the weighted, physical primary flux.

.. figure:: images/plots/simulation/simulated_primary_energy_level2.png

    : Primary energy distribution of the simulated CORSIKA Ehist IceProd datasets is shown on level 2. Not cuts or filters 
    are applied. This is not the entire statistics, but a subset of the data.


.. figure:: images/plots/simulation/simulated_primary_energy_level2_simweights_GaisserH3a.png

    : Primary energy distribution of the simulated CORSIKA Ehist IceProd datasets is shown on level 2. The weights are applied 
    using the GaisserH3a flux model.