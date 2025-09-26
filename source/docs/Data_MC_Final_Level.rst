.. _final level paragraph:
Data-MC Final Level
###################

The data-mc comparisons are performed on final level. From the years 2012, 2016 und 2020 the first and 15th day of each month is processed. This results in a total experimental livetime 
of :math:`2487\,\mathrm{h}`. The quality cuts used for level 5 are shown as a vertical black line in the plots. All plots also include the impact of the neutrinos, which are treated as background in 
this analysis. For the neutrino contamination, NuGen dataset for electrons, muons and taus 
are weighted with both atmospheric fluxes and an astrophysical component. For the atmospheric flux, 
the neutrinos are weighted with the respective cosmic-ray model. However, since the differences are very small, all predictions are presented in the same color (pink). For the astrophysical component, 
a single power law (SPL) with a normalizatoin of n = 1.8e-18 and a spectral index of gamma = 2.52 is assumed, resulting from `Measurement of the astrophysical diffuse neutrino flux
in a combined fit of IceCube’s high energy neutrino data <https://pos.sissa.it/444/1064/pdf>`_.

.. note::
    In :numref:`level3_rate_500TeV` the rates for the different primary flux models are shown for level 4. There is a mismatch of the normalization of the data and the MC.
    For the data-mc comparisons, the following plots use scaled weights. Therefore, the weights are normalized to the data for each weighting. This helps to analyze the shape of the different primary flux models. The rescaling is done based on the rates on final level.
    The rates and the rescaling factors are shown in :numref:`final_level_scale`.
    Additional data-mc plots to investigate cuts and all primary flux models are dumped `here <https://drive.google.com/drive/u/1/folders/1I2AD9wdWzaljAYM9xC5AESsnW1lxuq96>`_. For the unfolding, only the relative transition from the reconstructed proxy to the target variable matters, thus the **normalization** is completely **negligible**.

.. _final_level_scale:
.. list-table:: Rates on level 4 after applying the muon filter and a :math:`500\,\mathrm{TeV}` bundle energy cut at surface for different primary models and level 5 with the quality cuts are shown. The rescale factors are the ratio between the experimental rate and the MC rate. The rescaling is done based on the rates on level 4.
  :header-rows: 1

  * - Model
    - H3a
    - H4a
    - GST
    - GSF
    - Exp
  * - Level 4 / mHz
    - 21.62
    - 21.09
    - 20.92
    - 14.07
    - 18.55
  * - Rescale factor
    - 0.86
    - 0.88
    - 0.89
    - 1.32
    - 
  * - Level 5 / mHz
    - 15.16
    - 14.76
    - 14.79
    -  9.68
    - 12.36
  * - Rescale factor L5
    - 0.82
    - 0.84
    - 0.84
    - 1.28
    -
  * - Final Level / mHz
    - 1.29
    - 1.33
    - 1.09
    - 1.33
    - 1.41
  * - Rescale factor Final Level
    - 1.12
    - 1.09
    - 1.32
    - 1.09
    -

Seasonal Variations 
------------------- 

As presented in the analysis of Karolin Hymon, there are seasonal 
variations in the production of leptons in the atmosphere (`wiki page <https://user-web.icecube.wisc.edu/~khymon/SeasonalVariationsUnfolding/Index.html>`_). These variations are caused by the temperature and pressure changes in the atmosphere. Our new dataset allows us to investigate these variations, since we have simulated all 12 months/atmospheres per year (usually, only 4 atmospheres are simulated). The following plot :numref:`data_mc_finallevel_seasonal_variations` shows the rate per month for the different primary flux models. 


.. _data_mc_finallevel_seasonal_variations:
.. figure:: images/plots/selection/new/finallevel/rate_per_month_finallevel.png
    :width: 600px

    : Rate per month for different primary flux models.

As already mentioned above, there is a mismatch of the normalization of the data and the MC. 
In :numref:`data_mc_finallevel_seasonal_variations_rescaled`, the rates are rescaled. The shape is in agreement for all primary flux models. 

.. _data_mc_finallevel_seasonal_variations_rescaled:
.. figure:: images/plots/selection/new/finallevel/rate_per_month_finallevel_scaled_weights.png
    :width: 600px

    : Rate per month for different primary flux models with scaled weights.


.. note::
    The data-MC comparisons below are presented to investigate different properties of this dataset and
    the new DNN reconstructions after the quality cuts have been applied. However, for the unfolding, only the leading muon energy at entry is utilized, and thus, 
    data-MC mismatches in other variables do **not** affect the unfolding result. For the analysis, 
    only :numref:`data_mc_finallevel_leading_muon_energy_at_entry_GSF` is relevant.

Energy 
------

Bundle energy at entry 
++++++++++++++++++++++

.. _data_mc_finallevel_bundle_energy_at_entry_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_NuGen_astro_atmo_all_weightings.png
    :width: 600px

    : Bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``. 


Leading muon energy at entry 
++++++++++++++++++++++++++++

.. _data_mc_finallevel_leading_muon_energy_at_entry_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_NuGen_astro_atmo_all_weightings.png
    :width: 600px

    : Leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.



Bundle energy at surface 
++++++++++++++++++++++++

.. _data_mc_finallevel_bundle_energy_at_surface_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_NuGen_astro_atmo_all_weightings.png
    :width: 600px

    : Bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.


.. _data_mc_finallevel_bundle_energy_at_surface_precut_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_NuGen_astro_atmo_all_weightings.png
    :width: 600px

    : Bundle energy at surface reconstructed by pre-cut network  ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.


Leading muon energy at surface 
++++++++++++++++++++++++++++++

.. _data_mc_finallevel_leading_muon_energy_at_surface_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_NuGen_astro_atmo_all_weightings.png
    :width: 600px

    : Leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.


----

Energy uncertainty 
++++++++++++++++++

Bundle energy at entry - uncertainty
++++++++++++++++++++++++++++++++++++

.. _data_mc_finallevel_bundle_energy_at_entry_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_all_weightings.png
    :width: 600px

    : Uncertainty of bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.


Leading muon energy at entry - uncertainty
++++++++++++++++++++++++++++++++++++++++++

.. _data_mc_finallevel_leading_muon_energy_at_entry_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_all_weightings.png
    :width: 600px

    : Uncertainty of leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.



Bundle energy at surface - uncertainty
++++++++++++++++++++++++++++++++++++++

.. _data_mc_finallevel_bundle_energy_at_surface_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_all_weightings.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_finallevel_bundle_energy_at_surface_precut_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_log_uncertainty_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_all_weightings.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by pre-cut network ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.

Leading muon energy at surface - uncertainty
++++++++++++++++++++++++++++++++++++++++++++

.. _data_mc_finallevel_leading_muon_energy_surface_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_all_weightings.png
    :width: 600px

    : Uncertainty of leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.


Zenithsine zenith
+++++++++++++

.. _data_mc_finallevel_cos_zenith_all_weightings:
.. figure:: images/plots/selection/new/finallevel/data_mc_cos_zenith_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_all_weightings.png
    :width: 600px

    : Cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.


----

Zenith - uncertainty
++++++++++++++++++++

.. _data_mc_finallevel_cos_zenith_GSF_uncertainty:
.. figure:: images/plots/selection/new/finallevel/data_mc_cos_zenith_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_all_weightings.png
    :width: 600px

    : Uncertainty of zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.


Azimuth
-------

Azimuth 
+++++++

.. _data_mc_finallevel_azimuth_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_azimuth_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_all_weightings.png
    :width: 600px

    : Azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

----

Azimuth - uncertainty
+++++++++++++++++++++

.. _data_mc_finallevel_azimuth_GSF_uncertainty:
.. figure:: images/plots/selection/new/finallevel/data_mc_azimuth_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_all_weightings.png
    :width: 600px

    : Uncertainty of azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.


Center position 
---------------

Time 
++++

.. _data_mc_finallevel_center_pos_t_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_center_pos_t_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Center time reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Time - uncertainty
++++++++++++++++++

.. _data_mc_finallevel_center_pos_t_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_center_pos_t_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of center time reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position x 
+++++++++++

.. _data_mc_finallevel_center_pos_x_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_center_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.



Position x - uncertainty
++++++++++++++++++++++++

.. _data_mc_finallevel_center_pos_x_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_center_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position y
++++++++++

.. _data_mc_finallevel_center_pos_y_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_center_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position y - uncertainty
++++++++++++++++++++++++

.. _data_mc_finallevel_center_pos_y_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_center_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position z
++++++++++

Further investigations of the z-vertex can be found in the 
:ref:`Appendix/Z-vertex investigations (L5) <data_mc_finallevel_center_pos_z_investigation paragraph>`.

.. _data_mc_finallevel_center_pos_z_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_center_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position z - uncertainty
++++++++++++++++++++++++

.. _data_mc_finallevel_center_pos_z_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_center_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Entry position
--------------

Time 
++++

.. _data_mc_finallevel_entry_pos_t_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_entry_pos_t_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Entry time reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Time - uncertainty
++++++++++++++++++

.. _data_mc_finallevel_entry_pos_t_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_entry_pos_t_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of entry time reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position x
+++++++++++

.. _data_mc_finallevel_entry_pos_x_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_entry_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position x - uncertainty
++++++++++++++++++++++++

.. _data_mc_finallevel_entry_pos_x_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_entry_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position y
++++++++++

.. _data_mc_finallevel_entry_pos_y_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_entry_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position y - uncertainty
++++++++++++++++++++++++

.. _data_mc_finallevel_entry_pos_y_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_entry_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position z
++++++++++

Further investigations of the z-vertex can be found in the 
:ref:`Appendix/Z-vertex investigations (L5) <data_mc_finallevel_center_pos_z_investigation paragraph>`.

.. _data_mc_finallevel_entry_pos_z_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_entry_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position z - uncertainty
++++++++++++++++++++++++

.. _data_mc_finallevel_entry_pos_z_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_entry_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Propagation length
------------------

Total propagation length 
++++++++++++++++++++++++


.. _data_mc_finallevel_total_propagation_length_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_length_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Length in detector 
++++++++++++++++++

.. _data_mc_finallevel_length_in_detector_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_length_in_detector_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Total propagation length - uncertainty
++++++++++++++++++++++++++++++++++++++

.. _data_mc_finallevel_total_propagation_length_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_Length_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Length in detector - uncertainty
++++++++++++++++++++++++++++++++

.. _data_mc_finallevel_length_in_detector_uncertainty_GSF:
.. figure:: images/plots/selection/new/finallevel/data_mc_LengthInDetector_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_all_weightings.png
    :width: 600px

    : Uncertainty of length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.