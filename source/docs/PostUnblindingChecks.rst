Post-unblinding Checks - reduction of zenith range to 90°-110°
##############################################################

Motivation of strict zenith cut
+++++++++++++++++++++++++++++++

The unfolded ratios for September to November do not match in strength with the MCEq prediction based on the MSIS atmospheric model.
Investigating the neutrino rate per month also indicate that the raise increase faster than decrease in fall. This is possibly related to
the fast heating of the stratosphere in spring at the atmosphere around Antarctica. This process is related to pressure waves causing this so-called
Sudden Stratospheric Warming.

The European Centre for Medium-Range Weather Forecasts (ECMWF) collects temperature data of the stratosphere measured on hourly basis from
multiple experiments. The stratosphere consists of various pressure levels which each have their own temperature profile. More information
about the layers and corresponding muon (also relevant for neutrino production) can be found `in this paper <https://arxiv.org/pdf/1001.0776.pdf>`_.
The zenith range from 90°-120° corresponds to latitudes from 90°S to 30°S. an illustration of these locations across the sky will be uploaded soon.
The following plots depict the temperature profiles for various pressure levels relevant for neutrino production (dashed lines). The profiles
are compared to the monthly neutrino rate within the zenith range from 90°-110° (for explanation why this range is regarded see below).

.. image:: images_pass2/emcwf_numurates90-110_85S30E-1.png

.. image:: images_pass2/emcwf_numurates90-110_75S30E-1.png

.. image:: images_pass2/emcwf_numurates90-120_30E_combinedLats_zenithbands-1.png

The temperature profiles are in phase with the neutrino data up to latitudes of 50°S (zenith: 110°). Whereas the temperature profiles
are still in phase with the rates at 30hPa at 40°S, the pressure layers at 70hPa and 100hPa show are in opposite phase to the neutrino rate.
This effect is even stronger at 30°S. All displayed layers are relevant for neutrino production and the opposite phasal behavior can impact the seasonal variation result.
Especially the inverted pressure levels are contributing to the particle production. Production profiles versus slant depth are displayed `here <https://wiki.icecube.wisc.edu/images/c/c9/Fig5-Teff-definition.png>`_.
The same profile will be obtained for neutrinos with MCEq.
Cutting at the zenith region at 110° would yield an observation of larger variations, as can be observed in MCEq predicted ratios `here <https://user-web.icecube.wisc.edu/~khymon/SeasonalVariationsUnfolding/docs/Overview.html>`_.

The average monthly rate for zenith between 90°-110° is depicted below.

.. image:: images_pass2/average_numurates90-110-1.png

.. image:: images_pass2/average_relativenumurates_90-120vs90-110-1.png

The rate variation is not symmetric across the year. The cooling (corresponding to rate decrease) is longer than the sudden increase in rate starting in August.
In contrast to the split in austral summer and winter (jun-aug vs. dec-feb) as investigated by `Honda et al. <https://arxiv.org/abs/1502.03916>`_, a new split into seasons
based in similar rates is proposed: may-aug  vs. oct-jan. This ensures that the variations can be measured at its most extreme times in the year.

Reducing the data set to zenith angles between 90°-110° only cases a loss of 26% of events. The systematic uncertainty is recalculated for the updated range.
Studies on MC whether the unfold algorithm needs to be reoptimized is depicted in the sections below.

Unfolding of updated zenith range:

.. image:: images_pass2/unblinded_e3_12yr_may-aug_oct-jan_sys_90-110_ratio_cblind-1.png





MC study
++++++++

The feasibility of cutting the maximum zenith angle at 110° is evaluated on MC. Seasonal pseudo-data sets are generated from MCEq weights and unfolded.
The left plot shows unfolding with the algorithm trained as it was, for the zenth range of 90°-120°. The right plot shows the unfolding with retrained and
reoptimized DSEA for the zenith range between 90°-110°, where the same parameters remain optimal. The corresponding plots are shown in the next
subsection.

.. image:: images_pass2/pass2_estimationMC_mceq_sv_estimationOnMC_12yr_mceq_100000train_may-aug_oct-jan_90-110_ratio_year_sys-1.png
  :width: 49%

.. image:: images_pass2/pass2_estimationMC_mceq_sv_estimationOnMC_12yr_mceq_100000train_retrainedmay-aug_oct-jan_90-110_ratio_year_sys-1.png
  :width: 49%

The unfolded results are both compatible with each other and can retrieve the MCEq flux prediction for both seasons.

The comparison between unfolded ratio and MCEq prediction is evaluated as a :math:`\chi^2` goodness of fit as it was done previously.
All seasons are compatible with the prediction.
Again, left shows no retraining of DSEA, right the retraining of DSEA.

.. image:: images_pass2/ratio_mcequnfolding_mean_splineapprox_may-aug_mceqtheoryflux_withuncertaintyinfit_90-110no-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_mean_splineapprox_may-aug_mceqtheoryflux_withuncertaintyinfit_90-110_retrained-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_mean_splineapprox_oct-jan_mceqtheoryflux_withuncertaintyinfit_90-110-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_mean_splineapprox_oct-jan_mceqtheoryflux_withuncertaintyinfit_90-110_retrained-1.png
  :width: 49%


Systematic uncertainty
++++++++++++++++++++++

Calculated systematic uncertainties based on the cutted MC sample for 90°-110°:

.. image:: images_pass2/pass2_errorbar_newbns12yr_unblind_may-aug_sys_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_errorbar_newbns12yr_unblind_oct-jan_sys_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_erroroverview_unblind_may-aug_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_erroroverview_unblind_oct-jan_90-110-1.png
  :width: 49%

Re-optimization of the unfolding algorithm
++++++++++++++++++++++++++++++++++++++++++

The same Wasserstein Distance is achieved approx. as for the complete MC sample.
The same parameters are considered to remain as optimal.

.. image:: images_pass2/pass2_opt_2var_classifiers_default2_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_opt_2var_rf_exp_gridsearch_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_opt_2var_rf_expstartsize_gridsearch_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_opt_2var_rf_mul_gridsearch_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_opt_2var_rf_mul_gridsearch_extended_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_opt_2var_rf_leaves_gridsearch_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_opt_2var_rf_tau_gridsearch_ext_90-110-1.png
  :width: 49%

.. image:: images_pass2/pass2_opt_2var_rf_tau_gridsearch_90-110-1.png
  :width: 49%
