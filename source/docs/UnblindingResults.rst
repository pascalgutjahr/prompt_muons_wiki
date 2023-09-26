Unblinding Results
##################

The unblinded results will be displayed in this section. The use of the complete data set from 2011 (IC86) to 2022 has been approved. The complete data
sample contains 523736 events within 11.5 years of data.

Monthly spectra will be unfolded and its deviation from the annual average flux. The variation strength will be fitted per month and each energy bin.
The results will be compared to predictions from MCEq and the spectral index deviation from the annual average flux will be determined. Annual unfolding will
be performed to provide consistency between the years.

Monthly Neutrino Rate
+++++++++++++++++++++

In order to determine where the mismatch between unfolding and MCEq comes from in particular months, the neutrino rate is shown for
each month in the 12yr data sample.

.. image:: images_pass2/monthlyneutrinorate_2011-22_90-120-1.png


The first months of 2011 show a lower rate than the other years. This is likely to originate from the uncompleted detector setup.
The current IC-86 string configuration was completed at the end of 2010, but the run start including new detector setups is switching in May
for each year. This means that the additional seven strings are only included in the reconstruction from May onward, which results in a lower
rate for the respective month. Same behavior is observable below, where single years have been unfolded as post-unblinding crosschecks. Hence, the analysis is
shifted to 11.5 years of data starting from May 7, 2011.

Unfolded 11.5yr Spectra/Unfolded Ratios
+++++++++++++++++++++++++++++++++++++++

Shaded areas in the unfolded spectrum display systematic uncertainties. Statistical uncertainties are displayed by caps in the error bars.
A fit of spectral index shift is performed  on the ratio of seasonal flux to annual average flux. MCEq predictions are denoted as dashed lines.

.. image:: images_pass2/unblinded_e3_12yr_jun-aug_dec-feb_sys_90-120_ratio_cblind-1.png
  :width: 49%

.. image:: images_pass2/unblinded_e3_12yr_jan-jun_jul-dec_sys_90-120_ratio_cblind-1.png
  :width: 49%


.. list-table:: Significance per Season
   :widths: 25 25 50
   :header-rows: 1

   * - Season
     - TS
     - Significance / :math:`\sigma`
   * - jun-aug
     - -0.274
     - 3.3
   * - dec-feb
     - 0.179
     - 2.2
   * - jan-jun
     - -0.041
     - 1.2
   * - jul-dec
     - 0.038
     - 1.2



With spectral index shift fit:

.. image:: images_pass2/unblinded_e3_12yr_jun_jul_90-120_ratio_fit-1.png
  :width: 49%

.. image:: images_pass2/unblinded_e3_12yr_jan_dec_90-120_ratio_fit-1.png
  :width: 49%

.. image:: images_pass2/unblinded_e3_12yr_mar_apr_90-120_ratio_fit-1.png
  :width: 49%

.. image:: images_pass2/unblinded_e3_12yr_sep_oct_90-120_ratio_fit-1.png
  :width: 49%

.. image:: images_pass2/unblinded_e3_12yr_may_nov_90-120_ratio_fit-1.png
  :width: 49%

.. image:: images_pass2/unblinded_e3_12yr_feb_aug_90-120_ratio_fit-1.png
  :width: 49%

.. image:: images_pass2/unblinded_e3_12yr_mar-apr_sep-oct_90-120_ratio_fit-1.png
  :width: 49%

.. image:: images_pass2/unblinded_e3_12yr_jan-jun_jul-dec_90-120_ratio_fit-1.png
  :width: 49%


Comparison to MCEq:

.. image:: images_pass2/monthly_ratio_unblind_withmceq_jan_feb-1.png
  :width: 49%

.. image:: images_pass2/monthly_ratio_unblind_withmceq_mar_apr-1.png
  :width: 49%

.. image:: images_pass2/monthly_ratio_unblind_withmceq_may_jun-1.png
  :width: 49%

.. image:: images_pass2/monthly_ratio_unblind_withmceq_jul_aug-1.png
  :width: 49%

.. image:: images_pass2/monthly_ratio_unblind_withmceq_sep_oct-1.png
  :width: 49%

.. image:: images_pass2/monthly_ratio_unblind_withmceq_nov_dec-1.png
  :width: 49%

.. image:: images_pass2/monthly_ratio_unblind_withmceq_dec-jan_jun-jul-1.png
  :width: 49%

.. image:: images_pass2/monthly_ratio_unblind_withmceq_feb-mar_apr-may-1.png
  :width: 49%

.. image:: images_pass2/monthly_ratio_unblind_withmceq_aug-sep_oct-nov-1.png
  :width: 49%






Comparison of Unfolded Ratio to MCEq
++++++++++++++++++++++++++++++++++++

The unfolded ratios of seasonal to annual average flux are compared to predicted ratios by MCEq. This test has been performed on pseudo-data unfolding
and can be found `in the QA section <https://user-web.icecube.wisc.edu/~khymon/SeasonalVariationsUnfolding/docs/QA.html#questions-by-cosmic-ray-wg>`_.
The MCEq flux is calculated at the bin midth using the spline fits from the MCEq weighting. No uncertainty is considered on the  MCEq prediction, the statistical uncertainty is propagated to the ratio.
A linear fit is performed to determine whether both, the unfolded ratio and MCEq predictions, are compatible. A :math:`\chi^2`-test indicates whether
the unfolded result is represented by the MCEq prediction. The nullhypothesis of the unfolded result not following the MCEq prediction is only ruled out
by very small p-values. High p-values indicate that the nullhypothesis cannot be rejected to high significance.

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_jan_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_feb_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_mar_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_apr_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_may_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_jun_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_jul_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_aug_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_sep_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_oct_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_nov_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_dec_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_dec-feb_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_jun-aug_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_jan-jun_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%

.. image:: images_pass2/ratio_mcequnfolding_unblind_mean_jul-dec_mceqtheoryflux_withuncertaintyinfit-1.png
  :width: 49%


Fit of Variation Strength
+++++++++++++++++++++++++

As presented as post-unblinding plan in the Q&A section, the variations per energy bin and month are determined by a cosine fit:
:math:`A \cdot cos(b \cdot x)`. :math:`A` denotes the variation strength in the respective energy bin, :math:`b` denotes the period
of the cosine.
The caps denote the statistical uncertainties of the unfolded ratio of seasonal to annual average flux. Systematic uncertainty averages out,
as explained in the wiki. MCEq predictions are shown for comparison.

.. image:: images_pass2/unblind_ratio_bin1-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin2-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin3-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin4-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin5-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin6-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin7-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin8-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin9-1.png
  :width: 49%

.. image:: images_pass2/unblind_ratio_bin10-1.png
  :width: 49%

The fit fails for the first 3 energy bins. The discrepancy in fall (August to October) can be observed in the upper plots as well.
The period matches the MCEq prediction, however, the variations are shifted. Maximum and minimum deviate in most energy bins.



Split into Years
++++++++++++++++

These plots were done as crosschecks of the complete 12yrs data set from January 2011 to December 2022. This test revealed that runs from the IC86
string configuration were used.

It is clearly observable that the lower rate of early 2011 causes problems in the unfolded result. Splitting data in combination of three years
for summer and winter split (dec-feb vs jun-aug), the dec-feb unfolding yields lower rates than the average 12yr unfolding for the respective season.
This behavior is not observable for jun-aug, which is not affected by the changed string configuration.

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2011-13-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2014-16-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2017-19-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2020-22-1.png
  :width: 49%


.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2011-13_dec-feb-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2014-16_dec-feb-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2017-19_dec-feb-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2020-22_dec-feb-1.png
  :width: 49%


.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2011-13_jun.aug-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2014-16_jun.aug-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2017-19_jun.aug-1.png
  :width: 49%

.. image:: images_pass2/yaerlyunfolding_unblind_12yr_2020-22_jun.aug-1.png
  :width: 49%



Data-MC Agreement
+++++++++++++++++

The same data-MC is observable as for the burn sample.

.. image:: images_pass2/datavsmc_atmastro_unnormed_L5_nch.value_12yr_21002-1.png
  :width: 49%

.. image:: images_pass2/datavsmc_atmastro_unnormed_SplineMPEICTruncatedEnergySPICEMie_BINS_Neutrino.energy_12yr_21002-1.png
  :width: 49%

Zenith distribution:

.. image:: images_pass2/zenithdistribution_11.5yrs-1.png
  :width: 49%
