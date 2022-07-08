# Project Ideas

## From Felice Dunn

Fits to frequency of seeing data to determine how quantum efficiency, dark light, and threshold can trade for each other (Teich et al., 1982, Multiplication noise in the human visual system at threshold 3. The role of non-Poisson quantum fluctuations).

Model of the phototransduction cascade elements to demonstrate how single events can be amplified. Determine how the phototransduction elements and amplification can be changed to account for rod vs. cone responses. Use this model to predict responses to different stimuli types (Angueyra et al., 2022 Predicting and manipulating cone responses to naturalistic inputs)

Model different motion detectors and determine how they might be distinguishable from each other (Bae et al., 2014, Space-timing wiring specificity supports direction selectivity in the retina)

## From Jonathan Pillow

1. Temporal vs. rate coding in retina (or any other dataset you'd like to examine).
How much information is carried in the precise timing of spikes vs. in slowly-fluctuating spike rates?  One way to address this question is to decode spikes under models that incorporate vs. ignore precise spike timing information. 
Project idea;  compare decoding under an LNP model and a Poisson GLM with spike history filters. How much (if any) additional information can you recover about the stimulus when you incorporate spike history?

Relevant refs: 

 - Pillow et al. “Spatio-temporal correlations and visual signalling in a complete neuronal population”.  Nature (2008).

See also: GLM tutorial code (https://github.com/pillowlab/GLMspiketraintutorial).

2. Can a Poisson GLM exhibit divisive normalization?
Divisive normalization is one of the putative "canonical computations" carried out in the brain, but we still lack a good computational understanding of how it's carried out, or how to infer statistical models that can exhibit divisive normalization.
 
The Poisson generalized linear model (GLM) for spike trains provides a simple, tractable statistical model of spike trains. But can it exhibit divisive normalization?
 
Relevant refs: 

 - Carandini & Heeger,, Normalization as a canonical neural computation. Nat Rev Neurosci (2011).
 - Carandini and Heeger. Summation and division by neurons in primate visual cortex. Science (1994).
 - Pillow et al. “Spatio-temporal correlations and visual signalling in a complete neuronal population”.  Nature (2008).

## Lindsey Glickfeld

In [Barbera et al.](https://www.sciencedirect.com/science/article/pii/S0896627321007856), we used a simple subunit based, Hubel and Wiesel style model to predict V1 responses to gratings and plaids, and then to test the effect of mask phase on these responses. 

1.  This model built V1 cells that only have one (excitatory) subunit and orientation preference/selectivity is defined by the elongation of the long axis of the RF. However, V1 neurons typically have an "on" and an "off" subunit, and in the mouse orientation preference/selectivity is defined by the axis of overlap of these subunits. Build a new version of this model with on/off subunits and test whether this changes (A) the magnitude of cross orientation interactions and (B) the sensitivity of those interactions to mask phase.

2.  In cat/primate V1, plaid stimuli drive responses that are component selective.  However, in mouse V1, responses can be either pattern and component selective. Use this simple subunit model to (A) determine whether V1 neurons are component and/or pattern selective and (B) test whether these responses are sensitive to mask phase. 

The code for the model in Barbera et al. can be found here: https://figshare.com/collections/BarberaPriebeGlickfeld_Neuron_2022/5677225/ (Figure4_model _code.m)