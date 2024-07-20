.. _appendix paragraph:

Appendix
########

This appendix includes further information about studies, detailed investigations and tests.  

.. _stochasticity paragraph:

Stochasticity 
-------------

A muon loses its energy in stochastic processes. Thus, a single muon deposits stochastic energy losses along a track. In a bundle of many muons, 
every muon has its own stochastic energy losses, which 
appear as a more continuous energy loss in the detector. Hence, if there are very stochastic energy losses detected inside the detector, there are 
probably only a few muons or a single muon (at low energies). 
If we extend this to high energies, the largest energy losses are caused by the most energetic muon in the bundle. In a bundle in which the muon 
energies are distributed more equally, also the losses 
appear more continuously. The idea is to search for events that deposit their energy more stochastically to select and/or to improve the energy 
reconstruction of muons with a high leadingness. 

For the stochasticity calculation of the leading muon, the energy depositions and corresponding distances are needed. These can be determined by the function
`get_track_energy_depositions <https://github.com/icecube/ic3-labels/blob/5b68fa208607c5cba9cfd6ec317985017cc6c113/ic3_labels/labels/modules/event_generator/utils.py#L10>`_.
The stochasticity is then calculated by the function `compute_stochasticity <https://github.com/icecube/ic3-labels/blob/5b68fa208607c5cba9cfd6ec317985017cc6c113/ic3_labels/labels/modules/event_generator/utils.py#L796>`_.
This function calculates the stochasticity of energy losses along a track by measuring the area between the cumulative distribution function (CDF) of the energy losses 
and the relative distances. 
It returns three values: the stochasticity (a float between 0 and 1, normalized by 0.5), the total area above the diagonal (a float), and the total area below the diagonal (a float).
An extreme case of 1 means, the muon loses all it's energy in one interaction, the extreme case of 0 means, the muon loses all it's energy continuously.

As mentioned above, usually there is not only one muon, but several muons entering the detector. The energy losses of individual muons overlap. For this calculation, 
all energy losses of all muons with respect to their propagated distance are determined by the function 
`get_bundle_energy_depositions <https://github.com/icecube/ic3-labels/blob/5b68fa208607c5cba9cfd6ec317985017cc6c113/ic3_labels/labels/modules/event_generator/utils.py#L602>`_.
Here, it is assumed that all tracks travel on the same trajectory. The stochasticity is then calculated with the same function stated above. In this analysis, it is referred to 
as the bundle stochasticity.


Monte Carlo studies
+++++++++++++++++++

In :numref:`stochasticity_vs_leadingness`, the leadingness is shown as a function of the bundle stochasticity. If the muon event has a large stochasticity, 
this is caused by a high leadingness, but this is the case only for a small amount of events. Hence, a high leadingness does not necessary results to a 
large stochasticity.

.. _stochasticity_vs_leadingness:
.. figure:: images/plots/stochasticity_check/stochasticity_vs_leadingness.png

    : The leadingness is shown as a function of the bundle stochasticity as a weighted distribution.


To get an idea of the correlation between the leading muon energy and the bundle stochasticity, 
in :numref:`MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_entry_energy`, the energy of the leading muon is shown as a function of the bundle stochasticity.

.. _MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_entry_energy:
.. figure:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_entry_energy.png

    : The energy of the leading muon is shown as a function of the bundle stochasticity.

In the following, the title of the plots shows a cut applied on the bundle energy in GeV. Hence, from left to right only high energy muons are selected.

In :numref:`MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale`, 
the leadingness is shown as a function of the bundle stochasticity. High stochasticities lead to a large leadingness, but it removes the entire statistics.

.. _MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale:
.. figure:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.png

    : The leadingness is shown as a function of the bundle stochasticity.

In :numref:`MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale`, 
the leadingness is shown as a function of the largest energy loss. The largest energy loss is not a good indicator for the leadingness.

.. _MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale:
.. figure:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_leading_energy_rel_entry_bundle_energy_cuts_larger_bins_no_logscale.png

    : The leadingness is shown as a function of the largest energy loss.

In :numref:`MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_entry_energy`, the energy of the leading muon is shown as a function of the largest energy loss. 
The largest energy loss is correlated with the energy of the leading muon. The larger the energy loss, the higher the energy of the leading muon.

.. _MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_entry_energy:
.. figure:: images/plots/stochasticity_check/MCLabelsLeadingMuons_bundle_stochasticity_energy_00_vs_MCLabelsLeadingMuons_entry_energy.png

    : The energy of the leading muon is shown as a function of the largest energy loss.


In :numref:`bundle_muon_energy_spectrum_stochasticity_cuts`, the energy spectrum of the leading muon is shown for different cuts on the stochasticity. The plot is divided into 
a prompt and conventional component. 
A cut on the stochasticity removes high energy muons. Due to the low statistics expected at high energies for 10 years, 
we do not apply any cuts on the stochasticity in this analysis.

.. _bundle_muon_energy_spectrum_stochasticity_cuts:
.. figure:: images/plots/stochasticity_check/bundle_muon_energy_spectrum_stochasticity_cuts.png

    : The energy spectrum of the leading muon is shown for different cuts on the stochasticity.

.. _impact stochasticity paragraph:

Impact on the energy reconstruction
+++++++++++++++++++++++++++++++++++

The impact of the stochasticity on the energy reconstruction is shown in the following plots. 

The bundle energy reconstruction for different cuts on the stochasticity is shown in :numref:`bundleE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_lower` and
:numref:`bundleE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_higher`. A cut on the stochasticity does not improve the bundle energy reconstruction.

.. _bundleE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_lower:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundleE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_lower.png

    : The bundle energy reconstruction for stochasticities below a certain cut is shown.

.. _bundleE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_higher:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundleE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_higher.png
    
    : The bundle energy reconstruction for stochasticities above a certain cut is shown.

The leading muon energy reconstruction for different cuts on the stochasticity is shown in :numref:`leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_lower` and
:numref:`leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_higher`. A cut on the stochasticity does not improve the leading muon energy reconstruction.

.. _leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_lower:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_lower.png

    : The leading muon energy reconstruction for stochasticities below a certain cut is shown.

.. _leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_higher:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_stoch_cut_higher.png

    : The leading muon energy reconstruction for stochasticities above a certain cut is shown.

In summary, a cut on the stochasticity does not improve the bundle or leading muon energy reconstruction. 

.. _bundle radius paragraph:

Bundle radius 
-------------

Another idea to investigate muons with a high leadingness is to analyze the bundle radius. Depending on the fraction of the energy the most energetic muons carries, 
the projected radius of the 
entire bundle should differ. Here, different radii for the fractional amount of energy inside the projected area are studied. 
To quantify this, the perpendicular distance between the leading muon and the closest approach position to the center of the detector is 
calculated. Then, the closest approach point to the center is calculated for all muons in the bundle. With these positions, the distances between 
the leading muon and the other muons are calculated. Finally, the distances are weighted by the energy. For example, 100% means that the largest distance between 
a muon and the leading muon is considered. 90% means that the distance between the leading muon and the muon that accumulates 90 % of the bundle energy is considered.
In the following, this distance is referred to as the bundle radius. The calculation can be performed with the function 
`get_bundle_radius <https://github.com/icecube/ic3-labels/blob/5b68fa208607c5cba9cfd6ec317985017cc6c113/ic3_labels/labels/utils/muon.py#L1802>`_.

Monte Carlo studies
+++++++++++++++++++

In :numref:`bundle_radius_scale_2`, the bundle radius is shown for different bundle radius quantiles. These range from the energy inside the projected area 
from 50% to 100%. The same plot is shown for different scalings on the axes. The distributions peak between 5m and 20m, but also radii above 100m are observed.

.. _bundle_radius_scale_2:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_scale_2.png

    : The bundle radius is shown for different bundle radius quantiles.

In :numref:`bundle_radius_vs_leadingness`, the leadingness is shown as a function of the bundle radius for a bundle radius quantile of 100%. If the bundle radius is 
very small, the leadingness is high.

.. _bundle_radius_vs_leadingness:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_vs_leadingness.png

    : The leadingness is shown as a function of the bundle radius for a bundle radius quantile of 100% as a weighted distribution.

In the following :numref:`bundle_radius_radius_quantile_1.000_leadingness_bundle_energy_cut_no_logscale`, 
the leadingness is shown as a function of the bundle radius for different bundle energy cuts. If the bundle radius is high, the leadingness is low.

.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.500_leadingness_bundle_energy_cut_no_logscale.png 

.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.800_leadingness_bundle_energy_cut_no_logscale.png

.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.900_leadingness_bundle_energy_cut_no_logscale.png

.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.950_leadingness_bundle_energy_cut_no_logscale.png

.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_0.990_leadingness_bundle_energy_cut_no_logscale.png

.. _bundle_radius_radius_quantile_1.000_leadingness_bundle_energy_cut_no_logscale:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_1.000_leadingness_bundle_energy_cut_no_logscale.png

    : The leadingness is shown as a function of the bundle radius for different bundle energy cuts.

In :numref:`bundle_radius_radius_quantile_1.000_bundleE_bundle_energy_cut`, the muon bundle energy is shown as a function of the bundle radius for different bundle energy cuts.
For a small amount of events, a large bundle radius indicates a low bundle energy.

.. _bundle_radius_radius_quantile_1.000_bundleE_bundle_energy_cut:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_1.000_bundleE_bundle_energy_cut.png

    : The muon bundle energy is shown as a function of the bundle radius for different bundle energy cuts.

In :numref:`bundle_radius_radius_quantile_1.000_leadingE_bundle_energy_cut`, the leading muon energy is shown as a function of the bundle radius for different bundle energy cuts.
For a small amount of events, a large bundle radius indicates a low leading muon energy.

.. _bundle_radius_radius_quantile_1.000_leadingE_bundle_energy_cut:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_1.000_leadingE_bundle_energy_cut.png

    : The leading muon energy is shown as a function of the bundle radius for different bundle energy cuts.



In :numref:`leadingE_radius_0.990_cut_prompt`, the leading muon energy spectrum is shown for different cuts on the bundle radius. 
A bundle radius quantile of 99% is chosen as a cut parameter. 

.. _leadingE_radius_0.990_cut_prompt:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/leadingE_radius_0.990_cut_prompt.png

    : The leading muon energy spectrum is shown for different cuts on the bundle radius of the 99% quantile.

In :numref:`leadingE_radius_1.000_cut_prompt`, the leading muon energy spectrum is shown for different cuts on the bundle radius.
A bundle radius quantile of 100% is chosen as a cut parameter.

.. _leadingE_radius_1.000_cut_prompt:
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/leadingE_radius_1.000_cut_prompt.png

    : The leading muon energy spectrum is shown for different cuts on the bundle radius of the 100% quantile.


Selecting events below a certain bundle radius does not increase the sensitivity to distinguish between prompt and conventional, but it removes 
statistics. Thus, there is no selection performed using the bundle radius.

.. _impact bundle radius paragraph:

Impact on the energy reconstruction
+++++++++++++++++++++++++++++++++++

In :numref:`bundle_radius_radius_quantile_1.000_leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_radius_cut`, the impact of the bundle radius on the 
reconstruction of the leading muon energy is shown. A bundle radius quantile of 100% is chosen as a cut parameter.

.. _bundle_radius_radius_quantile_1.000_leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_radius_cut: 
.. figure:: images/plots/stochasticity_check_reco_bundle_radius/bundle_radius_radius_quantile_1.000_leadingE_DeepLearningReco_exported_model_PromptMu_L2_energy_radius_cut.png

    : The impact of the bundle radius of the 10% quantile on the reconstruction of the leading muon energy is shown.

There is no significant reconstruction improvement due to the application of a bundle radius cut. Instead, high energy 
events are rejected. Hence, no cut on the bundle radius is performed.