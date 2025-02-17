.. _data-mc level 5 paragraph:
Data-MC Level5
##############

The data-mc comparisons are performed on level 5. From the years 2012, 2016 und 2020 the first and 15th day of each month is processed. This results in a total experimental livetime 
of :math:`2487\,\mathrm{h}`. The quality cuts used for level 5 are shown as a vertical black line in the plots.

.. note::
    In :numref:`level3_rate_500TeV` the rates for the different primary flux models are shown for level 3. There is a mismatch of the normalization of the data and the MC.
    For the data-mc comparisons, the following plots use scaled weights. Therefore, the weights are normalized to the data for each weighting. This helps to analyze the shape of the different primary flux models. The rescaling is done based on the rates on level 4.
    The rates and the rescaling factors are shown in :numref:`level4_rate_500TeV_with_scale_`.
    Additional data-mc plots to investigate cuts and all primary flux models are dumped `here <https://drive.google.com/drive/u/1/folders/1I2AD9wdWzaljAYM9xC5AESsnW1lxuq96>`_.

.. _level4_rate_500TeV_with_scale_:
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

Seasonal Variations 
------------------- 

As presented in the analysis of Karolin Hymon, there are seasonal 
variations in the production of leptons in the atmosphere (`wiki page <https://user-web.icecube.wisc.edu/~khymon/SeasonalVariationsUnfolding/Index.html>`_). These variations are caused by the temperature and pressure changes in the atmosphere. Our new dataset allows us to investigate these variations, since we have simulated all 12 months/atmospheres per year (usually, only 4 atmospheres are simulated). The following plot :numref:`data_mc_L5_seasonal_variations` shows the rate per month for the different primary flux models. 


.. _data_mc_L5_seasonal_variations:
.. figure:: images/plots/data_mc/data_mc_level5/rate_per_month_level5.png
    :width: 600px

    : Rate per month for different primary flux models.

As already mentioned above, there is a mismatch of the normalization of the data and the MC. 
In :numref:`data_mc_L5_seasonal_variations_rescaled`, the rates are rescaled. The shape is in agreement for all primary flux models. 

.. _data_mc_L5_seasonal_variations_rescaled:
.. figure:: images/plots/data_mc/data_mc_level5/rate_per_month_level5_scaled_weights.png
    :width: 600px

    : Rate per month for different primary flux models with scaled weights.


Energy 
------

First of all, the energy distributions of the muon energy at surface and the reconstructed leading muon energy at entry is shown for the 
four different primary flux models to see their impact. 

.. figure:: images/plots/data_mc/data_mc_level5/primary_flux_ratio_MCLabelsLeadingMuons_muon_energy_first_mctree.png
    :width: 600px

    : Muon energy at surface for different primary flux models.

.. figure:: images/plots/data_mc/data_mc_level5/primary_flux_ratio_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy.png
    :width: 600px

    : Reconstructed muon energy at entry for different primary flux models
    (``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``).


Bundle energy at entry 
++++++++++++++++++++++



.. _data_mc_L5_bundle_energy_at_entry_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_GSF.png
    :width: 600px

    : Bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``. 

.. _data_mc_L5_bundle_energy_at_entry_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_GST.png
    :width: 600px

    : Bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``. 

.. _data_mc_L5_bundle_energy_at_entry_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_H3a.png
    :width: 600px

    : Bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_entry_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_H4a.png
    :width: 600px

    : Bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.


Leading muon energy at entry 
++++++++++++++++++++++++++++

.. _data_mc_L5_leading_muon_energy_at_entry_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_GSF.png
    :width: 600px

    : Leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_entry_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_GST.png
    :width: 600px

    : Leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_entry_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_H3a.png
    :width: 600px

    : Leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_entry_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_H4a.png
    :width: 600px

    : Leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.



Bundle energy at surface 
++++++++++++++++++++++++

.. _data_mc_L5_bundle_energy_at_surface_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_GSF.png
    :width: 600px

    : Bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_surface_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_GST.png
    :width: 600px

    : Bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_surface_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_H3a.png
    :width: 600px

    : Bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_surface_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_H4a.png
    :width: 600px

    : Bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_surface_precut_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_GSF.png
    :width: 600px

    : Bundle energy at surface reconstructed by pre-cut network  ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.

.. _data_mc_L5_bundle_energy_at_surface_precut_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_GST.png
    :width: 600px

    : Bundle energy at surface reconstructed by pre-cut network  ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.

.. _data_mc_L5_bundle_energy_at_surface_precut_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_H3a.png
    :width: 600px

    : Bundle energy at surface reconstructed by pre-cut network  ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.

.. _data_mc_L5_bundle_energy_at_surface_precut_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_H4a.png
    :width: 600px

    : Bundle energy at surface reconstructed by pre-cut network  ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.


Leading muon energy at surface 
++++++++++++++++++++++++++++++

.. _data_mc_L5_leading_muon_energy_at_surface_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_GSF.png
    :width: 600px

    : Leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_surface_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_GST.png
    :width: 600px

    : Leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_surface_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_H3a.png
    :width: 600px

    : Leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_surface_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_H4a.png
    :width: 600px

    : Leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.


----

Energy uncertainty 
++++++++++++++++++

Bundle energy at entry - uncertainty
++++++++++++++++++++++++++++++++++++

.. _data_mc_L5_bundle_energy_at_entry_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_GSF.png
    :width: 600px

    : Uncertainty of bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_entry_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_GST.png
    :width: 600px

    : Uncertainty of bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_entry_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_H3a.png
    :width: 600px

    : Uncertainty of bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_entry_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_H4a.png
    :width: 600px

    : Uncertainty of bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.


Leading muon energy at entry - uncertainty
++++++++++++++++++++++++++++++++++++++++++

.. _data_mc_L5_leading_muon_energy_at_entry_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_GSF.png
    :width: 600px

    : Uncertainty of leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_entry_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_GST.png
    :width: 600px

    : Uncertainty of leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_entry_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_H3a.png
    :width: 600px

    : Uncertainty of leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_at_entry_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_entry_energy_H4a.png
    :width: 600px

    : Uncertainty of leading muon energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.



Bundle energy at surface - uncertainty
++++++++++++++++++++++++++++++++++++++

.. _data_mc_L5_bundle_energy_at_surface_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_GSF.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_surface_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_GST.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_surface_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_H3a.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_surface_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_in_mctree_H4a.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_bundle_energy_at_surface_uncertainty_precut_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_GSF.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by pre-cut network ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.

.. _data_mc_L5_bundle_energy_at_surface_uncertainty_precut_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_GST.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by pre-cut network ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.

.. _data_mc_L5_bundle_energy_at_surface_uncertainty_precut_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_H3a.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by pre-cut network ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.

.. _data_mc_L5_bundle_energy_at_surface_uncertainty_precut_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01_bundle_energy_in_mctree_H4a.png
    :width: 600px

    : Uncertainty of bundle energy at surface reconstructed by pre-cut network ``DeepLearningReco_precut_surface_bundle_energy_3inputs_6ms_01``.

Leading muon energy at surface - uncertainty
++++++++++++++++++++++++++++++++++++++++++++

.. _data_mc_L5_leading_muon_energy_surface_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_GSF.png
    :width: 600px

    : Uncertainty of leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_surface_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_GST.png
    :width: 600px

    : Uncertainty of leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_surface_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_H3a.png
    :width: 600px

    : Uncertainty of leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_leading_muon_energy_surface_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_energy_hist_log_uncertainty_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_muon_energy_first_mctree_H4a.png
    :width: 600px

    : Uncertainty of leading muon energy at surface reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.


Zenith 
------

Cosine zenith
+++++++++++++

.. _data_mc_L5_cos_zenith_all_weightings:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_all_weightings.png
    :width: 600px

    : Cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.



.. _data_mc_L5_cos_zenith_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_GSF.png
    :width: 600px

    : Cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_cos_zenith_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_GST.png
    :width: 600px

    : Cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_cos_zenith_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_H3a.png
    :width: 600px

    : Cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_cos_zenith_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_H4a.png
    :width: 600px

    : Cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.
----

Zenith - uncertainty
++++++++++++++++++++

Cosine zenith - uncertainty
+++++++++++++++++++++++++++

.. _data_mc_L5_cos_zenith_GSF_uncertainty:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_GSF.png
    :width: 600px

    : Uncertainty of cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_cos_zenith_GST_uncertainty:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_GST.png
    :width: 600px

    : Uncertainty of cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_cos_zenith_H3a_uncertainty:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_H3a.png
    :width: 600px

    : Uncertainty of cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_cos_zenith_H4a_uncertainty:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_cos_zenith_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_H4a.png
    :width: 600px

    : Uncertainty of cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

Azimuth
-------

.. _data_mc_L5_azimuth_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_azimuth_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_GSF.png
    :width: 600px

    : Azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_azimuth_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_azimuth_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_GST.png
    :width: 600px

    : Azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_azimuth_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_azimuth_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_H3a.png
    :width: 600px

    : Azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_azimuth_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_azimuth_hist_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_H4a.png
    :width: 600px

    : Azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.



----

Azimuth - uncertainty
+++++++++++++++++++++

.. _data_mc_L5_azimuth_GSF_uncertainty:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_azimuth_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_GSF.png
    :width: 600px

    : Uncertainty of azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_azimuth_GST_uncertainty:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_azimuth_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_GST.png
    :width: 600px

    : Uncertainty of azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_azimuth_H3a_uncertainty:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_azimuth_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_H3a.png
    :width: 600px

    : Uncertainty of azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_azimuth_H4a_uncertainty:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_azimuth_hist_uncertainty_DeepLearningReco_direction_9inputs_6ms_medium_02_03_azimuth_H4a.png
    :width: 600px

    : Uncertainty of azimuth reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

Center position 
---------------

Time 
++++

.. _data_mc_L5_center_pos_t_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_t_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Center time reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Time - uncertainty
++++++++++++++++++

.. _data_mc_L5_center_pos_t_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_t_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of center time reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position x 
+++++++++++

.. _data_mc_L5_center_pos_x_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_x_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_x_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_x_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position x - uncertainty
++++++++++++++++++++++++

.. _data_mc_L5_center_pos_x_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_x_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Uncertainty of center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_x_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Uncertainty of center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_x_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Uncertainty of center position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.



Position y
++++++++++

.. _data_mc_L5_center_pos_y_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_y_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_y_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_y_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position y - uncertainty
++++++++++++++++++++++++

.. _data_mc_L5_center_pos_y_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_y_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Uncertainty of center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_y_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Uncertainty of center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_y_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Uncertainty of center position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position z
++++++++++

Further investigations of the z-vertex can be found in the 
:ref:`Appendix/Z-vertex investigations (L5) <data_mc_L5_center_pos_z_investigation paragraph>`.

.. _data_mc_L5_center_pos_z_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_z_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_z_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_z_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position z - uncertainty
++++++++++++++++++++++++

.. _data_mc_L5_center_pos_z_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_z_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Uncertainty of center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_z_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Uncertainty of center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_center_pos_z_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_center_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Uncertainty of center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Entry position
--------------

Time 
++++

.. _data_mc_L5_entry_pos_t_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_t_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Entry time reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Time - uncertainty
++++++++++++++++++

.. _data_mc_L5_entry_pos_t_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_t_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of entry time reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position x
+++++++++++

.. _data_mc_L5_entry_pos_x_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_x_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_x_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_x_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_x_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position x - uncertainty
++++++++++++++++++++++++

.. _data_mc_L5_entry_pos_x_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_x_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Uncertainty of entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_x_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Uncertainty of entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_x_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_x_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Uncertainty of entry position x reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position y
++++++++++

.. _data_mc_L5_entry_pos_y_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_y_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_y_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_y_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_y_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position y - uncertainty
++++++++++++++++++++++++

.. _data_mc_L5_entry_pos_y_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_y_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Uncertainty of entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_y_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Uncertainty of entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_y_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_y_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Uncertainty of entry position y reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Position z
++++++++++

Further investigations of the z-vertex can be found in the 
:ref:`Appendix/Z-vertex investigations (L5) <data_mc_L5_center_pos_z_investigation paragraph>`.

.. _data_mc_L5_entry_pos_z_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_z_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_z_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_z_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_z_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.


Position z - uncertainty
++++++++++++++++++++++++

.. _data_mc_L5_entry_pos_z_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_z_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Uncertainty of entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_z_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Uncertainty of entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_entry_pos_z_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_entry_pos_z_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Uncertainty of entry position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Propagation length
------------------

Total propagation length 
++++++++++++++++++++++++


.. _data_mc_L5_total_propagation_length_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_total_propagation_length_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_total_propagation_length_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_total_propagation_length_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Length in detector 
++++++++++++++++++

.. _data_mc_L5_length_in_detector_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_in_detector_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_length_in_detector_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_in_detector_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_length_in_detector_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_in_detector_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_length_in_detector_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_in_detector_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Total propagation length - uncertainty
++++++++++++++++++++++++++++++++++++++

.. _data_mc_L5_total_propagation_length_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_total_propagation_length_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Uncertainty of propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_total_propagation_length_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Uncertainty of propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_total_propagation_length_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_length_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Uncertainty of propagation length reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Length in detector - uncertainty
++++++++++++++++++++++++++++++++

.. _data_mc_L5_length_in_detector_uncertainty_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_LengthInDetector_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GSF.png
    :width: 600px

    : Uncertainty of length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_length_in_detector_uncertainty_GST:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_LengthInDetector_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_GST.png
    :width: 600px

    : Uncertainty of length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_length_in_detector_uncertainty_H3a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_LengthInDetector_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H3a.png
    :width: 600px

    : Uncertainty of length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_length_in_detector_uncertainty_H4a:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_LengthInDetector_uncertainty_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_H4a.png
    :width: 600px

    : Uncertainty of length in detector reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

Systematics
-----------

Detailed information about the systematics used for this analysis can 
be found :ref:`here <systematics_unfolding>`.

Further plots with all 4 primary models can be found in the Google docs `here <https://drive.google.com/drive/u/1/folders/1j7sUN6sYLJ1CpdZGJgEuajQNcStbZRsr>`_.

Bundle energy at entry
++++++++++++++++++++++

.. _data_mc_L5_sys_bundle_energy_at_entry_Absorption_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_energy_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_Absorption_GSF_5_sys_bins.png
    :width: 600px

    : Absorption effect on bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_sys_bundle_energy_at_entry_DOMEfficiency_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_energy_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_DOMEfficiency_GSF_5_sys_bins.png
    :width: 600px

    : DOM efficiency effect on bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_sys_bundle_energy_at_entry_HoleiceForward_Unified_p0_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_energy_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_HoleiceForward_Unified_p0_GSF_5_sys_bins.png
    :width: 600px 

    : Hole ice forward unified p0 effect on bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_sys_bundle_energy_at_entry_HoleiceForward_Unified_p1_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_energy_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_HoleiceForward_Unified_p1_GSF_5_sys_bins.png 
    :width: 600px

    : Hole ice forward unified p1 effect on bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

.. _data_mc_L5_sys_bundle_energy_at_entry_Scattering_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_energy_DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02_bundle_energy_at_entry_Scattering_GSF_5_sys_bins.png
    :width: 600px

    : Scattering effect on bundle energy at entry reconstructed by ``DeepLearningReco_leading_bundle_surface_leading_bundle_energy_OC_inputs9_6ms_large_log_02``.

Cosine zenith
+++++++++++++

.. _data_mc_L5_sys_cos_zenith_Absorption_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_Absorption_GSF_5_sys_bins.png
    :width: 600px

    : Absorption effect on cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_sys_cos_zenith_DOMEfficiency_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_DOMEfficiency_GSF_5_sys_bins.png
    :width: 600px

    : DOM efficiency effect on cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_sys_cos_zenith_HoleiceForward_Unified_p0_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_HoleIceForward_Unified_p0_GSF_5_sys_bins.png
    :width: 600px

    : Hole ice forward unified p0 effect on cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_sys_cos_zenith_HoleiceForward_Unified_p1_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_HoleIceForward_Unified_p1_GSF_5_sys_bins.png
    :width: 600px

    : Hole ice forward unified p1 effect on cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.

.. _data_mc_L5_sys_cos_zenith_Scattering_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_direction_9inputs_6ms_medium_02_03_cos_zenith_Scattering_GSF_5_sys_bins.png
    :width: 600px

    : Scattering effect on cosine zenith reconstructed by ``DeepLearningReco_direction_9inputs_6ms_medium_02_03``.


Center position z
+++++++++++++++++

.. _data_mc_L5_sys_center_pos_z_Absorption_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_center_pos_z_Absorption_GSF_5_sys_bins.png
    :width: 600px

    : Absorption effect on center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``. 

.. _data_mc_L5_sys_center_pos_z_DOMEfficiency_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_center_pos_z_DOMEfficiency_GSF_5_sys_bins.png
    :width: 600px 

    : DOM efficiency effect on center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_sys_center_pos_z_HoleiceForward_Unified_p0_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_center_pos_z_HoleIceForward_Unified_p0_GSF_5_sys_bins.png
    :width: 600px

    : Hole ice forward unified p0 effect on center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_sys_center_pos_z_HoleiceForward_Unified_p1_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_center_pos_z_HoleIceForward_Unified_p1_GSF_5_sys_bins.png
    :width: 600px

    : Hole ice forward unified p1 effect on center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.

.. _data_mc_L5_sys_center_pos_z_Scattering_GSF:
.. figure:: images/plots/data_mc/data_mc_level5/data_mc_sys_DeepLearningReco_track_geometry_9inputs_6ms_medium_01_center_pos_z_Scattering_GSF_5_sys_bins.png
    :width: 600px

    : Scattering effect on center position z reconstructed by ``DeepLearningReco_track_geometry_9inputs_6ms_medium_01``.