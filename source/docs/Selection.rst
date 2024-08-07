.. _selection paragraph:

Selection 
#########

The starting point for the selection is level 2.  
The rate for all events depends on the underlying primary model. For the common primary models, the rates are 1308 Hz (H3a), 1335 Hz (H4a), 1280 Hz (GST) and 1324 Hz (GSF). For example, using H3a, the number of total 
events per run (8h) can be estimated, which is 37,664,347. A single run 
is processed by a single processor unit. Assuming an average processing time 
of 1 second per event, the runtime per run would be 10462.32 hours, which 
is not feasible. Hence, a fast selection is necessary to remove 
statistics. As presented in :numref:`mceq_flux`, the prompt 
muon flux becomes more dominant towards higher energies, and it is 
suppressed by orders of magnitude at lower energies. Thus, low energy muons need 
to be removed. The rate of the prompt muons is 16 Hz (H3a), which makes 
1.2% of the total rate.

In a first step, several filters are investigated in regard 
to the energy of the leading muon at surface and the cosine zenith angle. The muon filter results as the best choice. Afterwards, a cut on the bundle energy at surface is applied to remove more low energy events. These two steps define 
level 3. In level 4, DNN reconstructions for several properties are added. 
In level 5, quality cuts are applied to improve the data-MC agreement.

**Note**
The rates mentioned above are based on the simulations 22774-22778. In this simulation, the lower 
energy bound of the primary energy is 10 TeV. Thus, the rates expected 
for the experimental data are higher, since also primaries with energies 
below 10 TeV produce muons that are detected by IceCube.

----

**old text**

The rate for all events is :math:`369.43\,\mathrm{Hz}`. This rate is dominated by the conventional component with 
:math:`365.21\,\mathrm{Hz}`. The prompt rate is :math:`4.23\,\mathrm{Hz}`.
The application of the muon filter leads to a rate of :math:`24.62\,\mathrm{Hz}`. This means, 708932 events are expected per run of 8h. 
If a single process step would take 1s per event, the runtime per run would be 197h, which is not feasible. If we target a runtime of 1h per run with 
a processing time of 1s per event, a rate of :math:`125\,\mathrm{mHz}` is required.

----

Level 3 
+++++++

Filters 
-------
The detection of atmospheric prompt muons requires high energy events. Thus, five different filters focusing on high energy events are tested to get rid of low energy events 
while keeping as many as possible high energy events. :numref:`fration_of_passed_events` shows the fraction of passed events for different energy bins, 
filters and weightings.

.. _leading_muon_energy_ratio:
.. figure:: images/plots/selection/filter_comparison_level2_MCLabelsLeadingMuons_muon_energy_first_mctree_simweights_GaisserH3a.png

    : Investigating the impact of several filters on level 2 for the leading muon energy at surface.

.. _cos_zenith_ratio:
.. figure:: images/plots/selection/filter_comparison_level2_MCLabelsLeadingMuons_PrimaryZenith_simweights_GaisserH3a.png

    : Investigating the impact of several filters on level 2 for the cosine of the primary zenith angle. 

.. _fration_of_passed_events:
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



In the final analysis, the lower bound of the muon energy at surface is 10 TeV. As presented in :numref:`fration_of_passed_events`, the MuonFilter 
rejects in total 98.8% of the events, but keeps the most events for the 4 energy intervals between 10 TeV and 100 PeV. Regarding the cosine zenith distribution, 
the HighQFilter removes more horizontal events than the MuonFilter. This is caused by the fact, that horizontal, high energy events travel through a large amount of 
ice and thus have a large amount of energy losses. In the detector, they are not able to pass the high-charge filter, since they arrive with a lower energy. 
Since we want to reconstruct the muon energy at surface, we want to keep these events.  
Hence, the MuonFilter is used.

The rates after the application of the MuonFilter are 15.24 Hz (H3a), 15.52 Hz (H4a), 14.88 Hz (GST) and 15.34 Hz (GSF). The number of events per run is 
438,942 (H3a). This results in a runtime of 122h per run with a processing time of 1s per event. This is still too long.


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