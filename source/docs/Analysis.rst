Analysis 
########

The entire analysis starts at Level2.

Selection 
+++++++++

Filters 
-------
The detection of atmospheric prompt muons requires high energy events. Thus, the MuonFilter and HQFilter are tested to get rid of low energy events 
while keeping as many as possible high energy events. 

.. image:: images/plots/pre_filter/bundle_muon_energy_ratio.pdf 

.. image:: images/plots/pre_filter/filter_fraction_bundle_muon.pdf

.. image:: images/plots/pre_filter/leading_muon_energy_ratio.pdf 

.. figure:: images/plots/pre_filter/filter_fraction_leading_muon.pdf

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
     
In the final analysis, the lower energy cut will probably be between :math:`10\,\mathrm{TeV}` and :math:`100\,\mathrm{TeV}`. Since we do not expect many events in 
total in this high energy regime for ten years of experimental data, the HQFilter rejects too many high-energetic events. 
For this analysis, we apply the MuonFilter, which rejects only :math:`6\,\%` of events above :math:`100\,\mathrm{TeV}`.

Leadingness 
-----------
Leadingness :math:`L_{\mathrm{E}}` describes the ratio of the highest energy muon :math:`E_{\mathrm{max}}` in a bundle to the total energy :math:`E_{\mathrm{tot}}` 
of the bundle:

.. math:: 

    L_{\mathrm{E}} = \frac{E_{\mathrm{max}}}{E_{\mathrm{tot}}}

.. image:: images/plots/dataset_exploration/leading_bundle_energy_fraction.pdf 

A minimum energy is required to have an excess of prompt particles in relation to conventional ones. In addition, there is a sweet spot between 
a leadingness of :math:`L_{\mathrm{E}} \in [0.1, 0.9]` in which the prompt component dominates the conventional component. Hence, a high leadingness does not 
lead to more sensitivity to detect prompt muons. This means, we are not searching for leading muons.

Leading vs. bundle energy 
-------------------------
The production of prompt an conventional particles is shown in relation to the GaisserH3a prediction. The GST and GSF model predict the 
most prompt muons.

.. image:: images/plots/dataset_exploration/prompt_production_primary_models.pdf

The energy spectra for the leading muon (most energetic muon inside a muon bundle) and muon bundle are presented for different primary models.

.. image:: images/plots/dataset_exploration/bundle_energy_at_entry_4_primary_models.pdf 

.. image:: images/plots/dataset_exploration/leading_energy_at_entry_4_primary_models.pdf

The GSF model is state-of-the-art and thus used in any plot, if only one primary weighting is shown. The leading muon energy is more sensitive to the prompt 
component in comparison to the muon bundle energy. 

.. image:: images/plots/dataset_exploration/pr_conv_MCLabelsLeadingMuons_bundle_energy_at_entry.pdf 

.. image:: images/plots/dataset_exploration/pr_conv_MCLabelsLeadingMuons_entry_energy.pdf



