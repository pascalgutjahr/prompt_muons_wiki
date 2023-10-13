Reconstructions 
###############

The reconstructions for the incoming direction and the energy of the muons are machine learning based using the `dnn_reco <https://github.com/icecube/dnn_reco>`_ framework.
The performance of the reconstructions is currently under investigation. So far, we had two bachelor students Leander Flottau and Benjamin Brandt working on angular and 
energy reconstructions. Their bachelor theses are provided on request. 
The networks mentioned below are the networks used for the plots stated in the Analysis chapter. Further below, the latest networks currently under investigation 
are presented


Networks used for analysis 
++++++++++++++++++++++++++

Angular reconstructions 
-----------------------
.. image:: images/plots/data_mc/DeepLearningReco_direction_big_PrimaryAzimuth.pdf

.. image:: images/plots/data_mc/DeepLearningReco_direction_big_PrimaryZenith.pdf

.. image:: images/plots/data_mc/DeepLearningReco_direction_big_PrimaryZenith_angle_deviation.pdf 

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

Some Monte Carlo studies are presented below. 

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_entry_energy.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_area_above_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_area_below_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_distance_00_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_distance_01_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_distance_02_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_01_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_02_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.pdf

.. image:: images/plots/stochasticity_check/bundle_muon_energy_spectrum_stochasticity_cuts.pdf




Bundle radius 
-------------

Another idea to investigate muons with a high leadingness is to analyze the bundle radius. Depending on the fraction of the energy the most energetic muons carries, the projected radius of the 
entire bundle should differ. Here, different radii for the fractional amount of energy inside the projected circle (first order approximation) are studied. 

