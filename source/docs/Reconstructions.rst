Reconstructions 
###############

The reconstructions for the incoming direction and the energy of the muons are machine learning based using the `dnn_reco <https://github.com/icecube/dnn_reco>`_ framework.
The performance of the reconstructions is currently under investigation. So far, we had two bachelor students Leander Flottau and Benjamin Brandt working on angular and 
energy reconstructions. Their bachelor theses are provided on request. 
The networks mentioned below are the networks used for the plots stated in the Analysis chapter. Further below, the latest networks currently under investigation 
are presented

The L2 muon filter is applied.

Input data 
++++++++++

The CNN structure provided in the IceCube framework is explained `here <https://iopscience.iop.org/article/10.1088/1748-0221/16/07/P07041>`_.

.. image:: images/dnn_input_cnn_paper.png

For the following reconstructions, three input features are used. Each of those are calculated per DOM:

* Total charge: Sum of charge 

* Relative time of first pulse: Relative to total time offset, calculated as the charge weighted mean time of all pulses

* Standard deviation of first pulse: Charge weighted standard deviation of pulse times relative to total time offset



Networks used for analysis 
++++++++++++++++++++++++++

Angular reconstructions 
-----------------------
.. image:: images/plots/data_mc/DeepLearningReco_direction_big_PrimaryAzimuth.pdf

.. image:: images/plots/data_mc/DeepLearningReco_direction_big_PrimaryZenith.pdf

.. image:: images/plots/data_mc/DeepLearningReco_direction_big_PrimaryZenith_angle_deviation.pdf 

Left side: only L2 muon filter, right side: L2 muon filter and cut on bundle energy: :math:`E > 10\,\mathrm{TeV}`

.. image:: images/plots/data_mc/zenith.pdf 
    :width: 49% 

.. image:: images/plots/data_mc/zenith_cut_1e4.pdf 
    :width: 49%


Energy reconstructions: muon bundle 
-----------------------------------
.. image:: images/plots/data_mc/DeepLearningReco_exported_model_PromptMu_L2_energy_bundle_energy_at_entry.pdf

.. image:: images/plots/data_mc/bundle_energy.pdf

Energy reconstruction: leading muon 
-----------------------------------
.. image:: images/plots/data_mc/DeepLearningReco_exported_model_PromptMu_L2_energy_entry_energy.pdf

.. image:: images/plots/data_mc/leading_energy.pdf

Multiplicity reconstruction 
---------------------------


Networks optimization 
+++++++++++++++++++++

The network optimization is currently under investigation.

Stochasticity 
-------------

A muon looses its energy in stochastic processes. Thus, a single muon deposits stochastic energy losses along a track. In a bundle of many muons, every muon has its own stochastic energy losses, which 
appear as a more continuous energy loss in the detector. Hence, if there are very stochastic energy losses detected inside the detector, there are probably only a few or maybe a single muon (at low energies). 
If we extend this to high energies, the largest energy losses are caused by the most energetic muon in the bundle. In a bundle in which the muon energies are distributed more equally, also the losses 
appear more continuously. The idea is to search for events that deposit their energy more stochastically to select and/or to improve the energy reconstruction of muons with a high leadingness. 

A full notebook with all plots can be found `here <https://github.com/icecube/dnn_selections/blob/AnalysisPipeline/notebooks/atmospheric_muon_leading/selection_performance/stochasticity_check.py.ipynb>`_.

Monte Carlo studies
-------------------

Some Monte Carlo studies are presented below. 

The rquirement of a minimum stochasticity removes low energy events. 

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_entry_energy.pdf

High stochasticities lead to a large leadingness, but it removes the entire statistics.

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_area_above_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_area_below_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_distance_00_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_distance_01_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_distance_02_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_01_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_02_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

Leading muon energy as a function of the largest energy loss: 

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_entry_energy.pdf


A cut on the stochasticity removes high energy muons. Due to the low statistics expected at high energies for 10 years, 
we do not apply any cuts on the stochasticity.

.. image:: images/plots/stochasticity_check/bundle_muon_energy_spectrum_stochasticity_cuts.pdf

Impact on the energy reconstruction
-----------------------------------

Bundle energy reconstruction:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundleE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_lower.pdf

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundleE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_higher.pdf

Leading muon energy reconstruction:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_lower.pdf

.. image:: images/plots/stochasticity_check_reco_bundle_radius/leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_higher.pdf

A cut on the stochasticity does not improve the bundle or leading muon energy reconstruction for the networks presented here. 


Bundle radius 
-------------

Another idea to investigate muons with a high leadingness is to analyze the bundle radius. Depending on the fraction of the energy the most energetic muons carries, the projected radius of the 
entire bundle should differ. Here, different radii for the fractional amount of energy inside the projected circle (first order approximation) are studied. 

A full notebook with all plots can be found `here <https://github.com/icecube/dnn_selections/blob/AnalysisPipeline/notebooks/atmospheric_muon_leading/selection_performance/stochasticity_check_reco_bundle_radius.ipynb>`_.

Monte Carlo studies
-------------------

Resulting bundle raddi:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_scale_2.pdf

Leadingness for different bundle radii:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.500_leadingness_bundle_energy_cut_no_logscale.pdf 

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.800_leadingness_bundle_energy_cut_no_logscale.pdf

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.900_leadingness_bundle_energy_cut_no_logscale.pdf

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.950_leadingness_bundle_energy_cut_no_logscale.pdf

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.990_leadingness_bundle_energy_cut_no_logscale.pdf

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_1.000_leadingness_bundle_energy_cut_no_logscale.pdf

As expected, a large bundle radius leads to a low leadingness. 

Leading muon energy as a function of the bundle radius for different bundle energy cuts:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_1.000_bundleE_bundle_energy_cut.pdf

Bundle muon energy as a function of the bundle radius for different bundle energy cuts:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_1.000_leadingE_bundle_energy_cut.pdf

Leading energy spectrum for different cuts:

* 99% bundle radius cut:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/leadingE_radius_0.990_cut_prompt.pdf

* 100% bundle radius cut:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/leadingE_radius_1.000_cut_prompt.pdf

A cut on the bundle radius also removes high energy events, thus we do not plan to set a cut.


Impact on the energy reconstruction
-----------------------------------

Leading muon energy reconstruction, 100% bundle radius:

.. image:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_1.000_leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_radius_cut.pdf

There is no significant reconstruction improvement due to the application of a bundle radius cut. Instead, high energy 
events are rejected.