.. _selection paragraph:

Selection 
#########

The starting point for the selection is level 2.  
The rate for all events is :math:`369.43\,\mathrm{Hz}`. This rate is dominated by the prompt component with 
:math:`365.21\,\mathrm{Hz}`. The prompt rate is :math:`4.23\,\mathrm{Hz}`.
The application of the muon filter leads to a rate of :math:`24.62\,\mathrm{Hz}`. This means, 708932 events are expected per run of 8h. 
If a single process step would take 1s per event, the runtime per run would be 197h, which is not feasible. If we target a runtime of 1h per run with 
a processing time of 1s per event, a rate of :math:`125\,\mathrm{mHz}` is required.

In the following, our level 3 containing the muon filter and an energy cut to reduce the rate is discussed. Afterwards, level 4 with the application of the DNN models is presented.
Level 5 is not yet defined and depends on the quality cuts of the data-mc comparison.


Level 3 
+++++++

Filters 
-------
The detection of atmospheric prompt muons requires high energy events. Thus, the MuonFilter and HQFilter are tested to get rid of low energy events 
while keeping as many as possible high energy events. :numref:`fration_of_rejected_events` shows the fraction of rejected events for different energy cuts.

.. _bundle_muon_energy_ratio:
.. figure:: images/plots/pre_filter/bundle_muon_energy_ratio.pdf

    : Investigating the impact of the muon and HQ filter on level 2 for the bundle energy at entry.

.. _leading_muon_energy_ratio:
.. figure:: images/plots/pre_filter/leading_muon_energy_ratio.pdf

    : Investigating the impact of the muon and HQ filter on level 2 for the leading muon energy at entry.

.. _fration_of_rejected_events:
.. list-table:: Fraction of rejected events 
    :widths: 33 33 33 33
    :header-rows: 1 

    * - 
      - All energies 
      - Leading energy :math:`> 10\,\mathrm{TeV}`
      - Leading energy :math:`> 100\,\mathrm{TeV}`
    * - MuonFilter 
      - 0.93 
      - 0.28 
      - 0.06 
    * - HQFilter 
      - 0.99 
      - 0.74 
      - 0.18

Energy Bins and Weights
=======================

.. list-table:: Fraction of events passed filters for different energy bins and weightings. Muon energy at surface is considered.
   :header-rows: 1

   * - Filter
     - 10 TeV < E < 100 TeV
     - 100 TeV < E < 1 PeV
     - 1 PeV < E < 10 PeV
     - 10 PeV < E < 100 PeV 
     - All energies
   * - MuonFilter, GaisserH3a
     - 2.8e-01
     - 7.8e-01
     - 8.3e-01
     - 1.0e+00
     - 1.2e-02
   * - OnlineL2Filter, GaisserH3a
     - 1.2e-01
     - 6.3e-01
     - 7.9e-01
     - 8.6e-01
     - 2.9e-03
   * - HighQFilter, GaisserH3a
     - 3.0e-02
     - 2.8e-01
     - 5.1e-01
     - 6.4e-01
     - 5.1e-04
   * - EHEAlertFilter, GaisserH3a
     - 0.0e+00
     - 1.8e-07
     - 2.0e-05
     - 0.0e+00
     - 4.6e-12
   * - EHEAlertFilterHB, GaisserH3a
     - 2.9e-06
     - 8.3e-04
     - 3.2e-02
     - 2.1e-01
     - 4.4e-08
   * - MuonFilter, GaisserH4a
     - 2.8e-01
     - 7.8e-01
     - 8.0e-01
     - 1.0e+00
     - 1.2e-02
   * - OnlineL2Filter, GaisserH4a
     - 1.2e-01
     - 6.3e-01
     - 7.7e-01
     - 1.0e+00
     - 2.8e-03
   * - HighQFilter, GaisserH4a
     - 2.9e-02
     - 2.7e-01
     - 5.2e-01
     - 6.5e-01
     - 5.0e-04
   * - EHEAlertFilter, GaisserH4a
     - 0.0e+00
     - 1.8e-07
     - 1.2e-04
     - 0.0e+00
     - 7.4e-12
   * - EHEAlertFilterHB, GaisserH4a
     - 2.4e-06
     - 6.5e-04
     - 2.2e-02
     - 2.6e-01
     - 3.6e-08
   * - MuonFilter, GlobalFitGST
     - 2.9e-01
     - 7.8e-01
     - 8.4e-01
     - 1.0e+00
     - 1.1e-02
   * - OnlineL2Filter, GlobalFitGST
     - 1.3e-01
     - 6.3e-01
     - 8.2e-01
     - 1.0e+00
     - 2.7e-03
   * - HighQFilter, GlobalFitGST
     - 3.3e-02
     - 2.9e-01
     - 5.1e-01
     - 6.4e-01
     - 5.4e-04
   * - EHEAlertFilter, GlobalFitGST
     - 0.0e+00
     - 2.4e-07
     - 2.6e-10
     - 0.0e+00
     - 4.4e-12
   * - EHEAlertFilterHB, GlobalFitGST
     - 2.2e-06
     - 5.2e-04
     - 3.0e-02
     - 3.1e-01
     - 2.7e-08
   * - MuonFilter, GlobalSplineFit5Comp
     - 2.7e-01
     - 7.8e-01
     - 7.6e-01
     - 1.0e+00
     - 1.2e-02
   * - OnlineL2Filter, GlobalSplineFit5Comp
     - 1.2e-01
     - 6.2e-01
     - 7.3e-01
     - 9.5e-01
     - 2.6e-03
   * - HighQFilter, GlobalSplineFit5Comp
     - 2.6e-02
     - 2.7e-01
     - 5.6e-01
     - 6.1e-01
     - 4.1e-04
   * - EHEAlertFilter, GlobalSplineFit5Comp
     - 0.0e+00
     - 9.7e-08
     - 2.4e-05
     - 0.0e+00
     - 3.3e-12
   * - EHEAlertFilterHB, GlobalSplineFit5Comp
     - 1.7e-06
     - 4.0e-04
     - 2.7e-02
     - 3.0e-01
     - 2.5e-08



     
In the final analysis, the lower energy cut will probably be between :math:`10\,\mathrm{TeV}` and :math:`100\,\mathrm{TeV}`. Since we do not expect many events in 
total in this high energy regime for ten years of experimental data, the HQFilter rejects too many high-energetic events. 
For this analysis, we apply the MuonFilter, which rejects only :math:`6\,\%` of events above :math:`100\,\mathrm{TeV}` (leading muon energy at entry). The corresponding 
energy cut for each network is shown in the legend.


Bundle energy pre cut 
---------------------
To further reduce the number of events in the low energy region, a cut on the bundle energy at surface is applied. For this, 
the efficiency as a ratio of the number of events before and after the cut is calculated. The efficiency is shown for 
different zenith ranges. The cut is applied in a way, that the remaining rate is :math:`125\,\mathrm{mHz}`.

.. _efficiency_comparison__bundle_energy_in_mctree_zenith_0_90:
.. figure:: images/plots/model_evaluation/precut/efficiency_comparison__bundle_energy_in_mctree_zenith_0_90.pdf

    : Events left after application of a muon bundle cut for a zenith range of 0 to 90 degrees.

.. _efficiency_comparison__bundle_energy_in_mctree_zenith_0_45:
.. figure:: images/plots/model_evaluation/precut/efficiency_comparison__bundle_energy_in_mctree_zenith_0_45.pdf

    : Events left after application of a muon bundle cut for a zenith range of 0 to 45 degrees.

.. _efficiency_comparison__bundle_energy_in_mctree_zenith_70_90:
.. figure:: images/plots/model_evaluation/precut/efficiency_comparison__bundle_energy_in_mctree_zenith_70_90.pdf

    : Events left after application of a muon bundle cut for a zenith range of 70 to 90 degrees.

For the first 17 networks, a cut on the bundle energy at entry is applied. But for large zenith angles, high energy events are removed that appear as low energy events in the detector 
due to the large path length through the earth and thus the accumulated energy losses. Hence, the last two (red and dark red) networks apply a cut on the bundle energy at surface.
In :numref:`efficiency_comparison__bundle_energy_in_mctree_zenith_70_90`, the efficiency is shown for a zenith range of :math:`70` to :math:`90` degrees. This plot proofs this statement.
The cuts are :math:`211\,\mathrm{TeV}` and :math:`228\,\mathrm{TeV}`. 

For our level 3, we apply the MuonFilter and a cut of :math:`200\,\mathrm{TeV}` on the bundle energy at surface. The remaining rate is :math:`144.3\,\mathrm{mHz}`. The network 
``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01`` is used. 

Level 4 
+++++++

On level 4, we do not apply any filters and we do not remove any events. We just add the DNN reconstructions mentioned in the reconstruction section. For this, the following networks are added:

* ``DeepLearningReco_direction_9inputs_uncleaned_medium_01``
* ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_large_log_02``
* ``DeepLearningReco_track_geometry_9inputs_uncleaned_01``

Already added in step 3:

* ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``

In :numref:`DNN_reconstruction_runtimes`, the runtimes for the DNN reconstructions are shown. The preprocessing time is needed to create the input features for the DNNs based on the 
input pulses. The preprocessing time of the precut network is faster, since only 3 input features instead of 9 features are calculated. 
The CPU and GPU times are the runtimes needed to apply the DNNs on the respective device.

.. _DNN_reconstruction_runtimes:
.. list-table:: DNN reconstruction runtimes 
    :widths: 33 33 33 33
    :header-rows: 1 

    * - Network
      - Preprocessing / ms 
      - CPU / ms 
      - GPU / ms
    * - Direction
      - 22 ± 20  
      - 106 ± 42 
      - 5 ± 38 
    * - Energy 
      - 22 ± 20
      - 144 ± 56 
      - 3 ± 13 
    * - Track geometry
      - 22 ± 20 
      - 106 ± 42 
      - 3 ± 10
    * - precut 
      -  1 ± 1
      - 11 ± 1
      - 7 ± 4

Level 5
+++++++

- level not yet defined, depends on quality cuts of data-mc comparison