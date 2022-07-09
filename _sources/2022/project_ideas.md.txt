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

The code for the model in Barbera et al. can be found here: https://figshare.com/collections/BarberaPriebeGlickfeld_Neuron_2022/5677225/ see Figure4_model_code.m

## Emily Cooper

I’ve shared a (non-exhaustive) list of some public databases of natural images, depth maps, and eye movements that may be useful for projects here:

https://docs.google.com/document/d/1bVTdvXXoGN4Ya4mutdEBQOQdmO6tc68uHHIccrvdlTI/edit?usp=sharing

Project suggestion 1: What does your next fixation point look like? 
Using the DOVES dataset of eye movements during free-viewing of calibrated natural images (see Google Doc; https://live.ece.utexas.edu/research/doves/), select pairs of fixation points in temporal sequence and create small image patches centered on those fixation points. Characterize the visual similarity (or dissimilarity) of these pairs of sequentially fixated image patches using any approaches you’d like (e.g., mutual information, difference in slope of Fourier power spectrum, difference in orientation spectrum, difference in RMS contrast, SSIM). Next, compare the distribution of these measures to a distribution derived from randomly selected pairs of image patches. Are sequentially fixated image patches more similar or different from random pairs of image patches based on any of these measures? Be sure to control for the distance between pairs (image patches that are closer to each other are known to be more similar). If you do find a pattern, does it extend to fixated points with larger separations in time? You could try this analysis on one of the other eye movements datasets, but keep in mind that the pixel intensity values in Hollywood movies are not necessarily linear with respect to light in the world.

Project suggestion 2: How far away is your next fixation?
When engaged in natural tasks, people tend to fixate points that are relatively close to them, as compared to a random sample of points from their surrounding environment. Using the UT Austin Natural Image Databases (see Google Doc; https://natural-scenes.cps.utexas.edu/db.shtml – just the subset with co-registered images and depth maps, scroll down to “Stereo Image and Range Data Collection”), investigate potential low level fixation strategies that might recapitulate this behavior. First, simulate a set of random fixation points and plot the distribution of associated scene distances from the depth maps – this should generally match the overall distribution of distances found in the scenes. Next, try biasing your fixation points based on low level properties of the co-registered images run the scene images. For example, you could run the images through an edge detection algorithm and select a random sample of points that fall on luminance edges. You could calculate the local RMS contrast of points and weight your fixation sampling strategy towards higher contrast image regions. You could even assert that people only fixate points that are red. Do any of these strategies result in the near-distance bias we observe in natural fixations?  

## EJ Chichilnisky

download Pillow data set, fit GLM. test if we can do better with some kind of subunit model fit (Shah 2020 paper)?

## Marlene Cohen

Generate a fake multineuron data set. This should include spike count, BOLD, or calcium imaging responses of n neurons (or voxels) on m trials. You could use models from any of several tutorials to generate these responses. (I know that ChoiceProbabilityTutorial will do this for a population of MT neurons.) From this fake data set, calculate:

1) the average correlation between each pair of neurons (this could be noise or signal correlation, depending on the data set you generated)

2) the dimensionality of the shared variability (e.g. by calculating the proportion variance explained by the first k principal components for k=1:n)

3) for the overachievers among you, calculate some fancy measurements too, such as communication subspace dimensionality if you modeled multiple brain areas (good code here: https://github.com/joao-semedo/communication-subspace) or average or modal controllability (good code at #3 here: https://complexsystemsupenn.com/codedata ; start with the correlation matrix with the diagonal set to 0 instead of 1). If you would like to experiment with topological data analysis, I can provide code for that too.

Next, make some change to your model that will affect the shared variability (maybe add in a common noise source, or change some model parameters) and repeat the calculations in #1-3. Can you gain some insight into how those numbers are related?

Possible publishable extension: Do these calculations in a real data set (yours? Or several from my lab are available if you would like). Which ways of quantifying shared variability are most closely associated with behavior, stimuli, task condition, or some other quantity you think is important?

## Eero Simoncelli

(note from Dan: not really a project idea, but a tool you could use in a project)
My lab has produced a python library of tools to explore vision models by  synthesizing novel informative images.
This includes Metamers (as per my talk yesterday), Eigendistortions (Berardino 2017), Maximal differentiation (MAD) competition (Wang 2008), and Geodesics (Henaff 2016). Might be useful for some students in the course.  If you want to link it from Slack or from the course GitHub, it’s here: https://github.com/LabForComputationalVision/plenoptic/. Kate Bonnen is an expert user and someone to ask questions about it.