Q & A
#####

* October 21, 2023

`Q: How do you want to identify a prompt muon?`

A: We do not want do identify a prompt muon. We want to measure the normalization of the prompt component. 

----

`Q: Is 20 % offset between MCEq and CORSIKA an issue?` 

A: These are two completely different approaches. There is no true or correct result. (see section `Definitions of the prompt component`)

----

`Q: How does the cos(theta) distribution behaves in comparison with the results of Patrick Berghaus?`

A: There are similar issues. Overshoots above 0.5 and undershoots around 0.3.

----

`Q: Do you set a fixed conventional normalization in your pseudo analysis? If not, to which value do you fit it?`

A: No, it is not fixed. In the pseudo analysis we fit it to 0.998.

----

`Q: What happens, if you use single muons?`

A: For the pseudo analysis, we use the reconstructed bundle energy at entry to fit the normalization of the prompt and conventional muon flux. Here, we do not select 
muons with a special leadingness. This follows from :numref:`leading_bundle_energy_fraction`, which shows that a high leadingness does not increase the sensitivity do detect prompt 
muons. Apart from that, a single muon does not appear at high energies, there you only have muon bundles. If we select muons with a high leadingness, often referred to as 
single muons, we would lose statistics and the analysis would be less sensitive.

----

`Q: Regarding the zenith-problem: Maybe you can estimate the impact of the magnetic field of the earth on high energy muons. Could this help to solve the problem?` 

A: TODO

----

`Q: How large are the uncertainties on the conventional component (pion/kaon production)?` 

A: TODO

----

`Q: How large is the background that we expect (astrophysical neutrinos, atmospheric neutrinos)? If we are able to distinguish between a single muon 
and a muon bundle, we can remove neutrino induced background muons.`

A: TODO

----

* September 29, 2023

`Q: In the simulation you remove the electromagnetic shower component. Thus, you also remove some muons. How large is the impact of this to your analysis?``

A: We used CORSIKA 8 to estimate the impact of the electromagnetic shower component on the produced muons. For a 500 PeV proton shower, the total amount of 
muon-energy per shower is about 4.8 %. 
For the large-scale simulation 
we will simulate the EM component, if the simulation of the EM component is feasible. This impact was investigated by Jean-Marco and is shown in 
:numref:`energy_distribution` and :numref:`num_and_energy_ratio`.

.. _energy_distribution:
.. figure:: images/plots/QA/energy_distribution.pdf 

    : CORSIKA 8 was used to simulate 500 PeV proton showers to estimate the impact of the electromagnetic shower component. 

.. _num_and_energy_ratio:
.. figure:: images/plots/QA/num_and_energy_ratio.pdf

    : The ratio of the number of muons and the energy of the muons is shown for 500 PeV proton showers. On average, 4.8 % of the energy is carried by muons originating 
    from the electromagnetic shower component.

----

`Q: Your prompt definition is: parent is not pion or kaon. The definiton in MCEq divides prompt and conventional by a minimum decay length of 0.123 cm. Is there a difference?`

A: The “lifetime” definition is similar, as it includes every particle with a lifetime which is greater than ten times the lifetime of the D0 as conventional and the rest as 
prompt. This is the definition of prompt used inside MCEq, and the lifetime limit corresponds to a decay length of approximately 1.2 cm. Considering all particles in CORSIKA7, 
these are the photon, electron, muon and neutrino from the fundamental particles. Of these none can decay into a muon. But in CORSIKA, a muon can be listed as 
the parent of a muon. These would then be considered to belong to the conventional component. The hadrons below the lifetime limit are pion, K±, KL, KS, which are exactly the pion 
and kaons from the pion-kaon definition. The Baryons below the lifetime limit are 𝑝, 𝑛, 𝛬, 𝛴±, 𝛯0, 𝛯±, of these only the proton and the neutron can not decay into a muon. 
These baryons and the muon is the only difference compared to the pion-kaon definition of prompt. These particles do not seem to contribute much to the flux, as both of the 
definitions produce nearly identical results, see section `Definitions of the prompt component`.

----

`Q: How do you plan to reconstruct the leading muon energy?`

A: For the reconstruction of the leading muon energy, we use a convolutional neural network. Further details can be found in the `Reconstructions` section of this wiki.

----

`Q: In your pseudo analysis you used a poisson likelihood. Do you want to add limited statistics to your likelihood?`

A: Yes, we do want use the Say likelihood. Apart from that, for the real analysis we will probably switch to the tool NNMFit. This is already known in IceCube and in our 
first test it seems to work for us as well. Thus, we can avoid code duplication. In addition, the tools is able to perform fits with multiple datasets. In the future, this 
helps do to a combined fit with a atmospheric muon and neutrino dataset.

----

`Q: What is the impact of limited MC statistics on your analysis currently?`

A: As you can see in the section `New CORSIKA extended history simulations`, we have a quite sufficient statistics for high energies, but to little statistics for low energies. 
Hence, especially the low energy events are oversampled in the pseudo dataset. For the real analysis, we will simulate a new datasets with more statistics to reach 
statistical uncertainties lower than our systematic uncertainties. But to estimate our systematic uncertainties, we already need more statistics.