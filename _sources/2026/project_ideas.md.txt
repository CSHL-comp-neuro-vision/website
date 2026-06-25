# Project Ideas

## Flatiron Resources

Billy Broderick and Edoardo Balzani will join us from the Flatiron Institute to share two open source software packages that you may find helpful for your projects. 

* [NeMoS (Neural ModelS)](https://nemos.readthedocs.io/en/latest/) is a statistical modeling framework optimized for systems neuroscience and powered by jax. It streamlines the process of defining and selecting models, through a collection of easy-to-use methods for feature design. A NeMoS port of Jonathan Pillow’s GLM tutorials can be found [here](https://balzaniedoardo.github.io/nemos_glm_tutorials/index.html). 

* [Plenoptic](https://docs.plenoptic.org/docs/tags/2.0.0/) is a python library for model-based synthesis of perceptual stimuli, built on top of pytorch. For any pytorch model, users can generate stimuli which enable interpretation of model properties through examination of features that are enhanced, suppressed, or discarded. These stimuli can then be used in follow up experiments to validate or falsify model predictions. plenoptic also contains pytorch implementations of some vision models and image-processing tools, such as the Steerable Pyramid and the Portilla-Simonelli texture model.

Their group has an additional resource they will not share in the tutorials that you may find useful for your projects or research.

* [Pynapple](https://pynapple.org/) is a light-weight python library for neurophysiological data analysis. The goal is to offer a versatile set of tools to study typical data in the field, i.e. time series (spike times, behavioral events, etc.) and time intervals (trials, brain states, etc.). It also provides users with generic functions for neuroscience such as tuning curves, cross-correlograms and filtering.


## Tony Movshon

## E.J. Chichilnisky

## Eero Simoncelli

## Stephanie Palmer

## Jonathan Pillow

1. Temporal vs. rate coding in retina (or any other dataset you'd like to examine).
How much information is carried in the precise timing of spikes vs. in slowly-fluctuating spike rates?  One way to address this question is to decode spikes under models that incorporate vs. ignore precise spike timing information. 
Project idea;  compare decoding under an LNP model and a Poisson GLM with spike history filters. How much (if any) additional information can you recover about the stimulus when you incorporate spike history?

Relevant refs:

* <a href="../_static/pdfs/pillow/Pillow_etal_2008.pdf">Pillow et al. “Spatio-temporal correlations and visual signalling in a complete neuronal population”. </a>
* See also: [GLM tutorial code](https://github.com/pillowlab/GLMspiketraintutorial).

2. Can a Poisson GLM exhibit divisive normalization?
Divisive normalization is one of the putative "canonical computations" carried out in the brain, but we still lack a good computational understanding of how it's carried out, or how to infer statistical models that can exhibit divisive normalization.
 
The Poisson generalized linear model (GLM) for spike trains provides a simple, tractable statistical model of spike trains. But can it exhibit divisive normalization?
 
Relevant refs: 

* <a href="../_static/pdfs/pillow/carandini-heeger-2011-natrevneuro.pdf">Carandini & Heeger (2011) Normalization as a canonical neural computation. _Nat Rev Neurosci, 13_:51-62. DOI:10.1038/nrn3136.</a>
* <a href="../_static/pdfs/pillow/carandini-heeger-1994-science.pdf">Carandini & Heeger. (1994). Summation and division by neurons in primate visual cortex. _Science, 264_(5183):1333-1336. DOI:10.1126/science.8191289.</a>
* <a href="../_static/pdfs/pillow/Pillow_etal_2008.pdf">Pillow et al. (2008). Spatio-temporal correlations and visual signalling in a complete neuronal population. _Nature, 454_(21). DOI:10.1038/nature07140.</a>

 3. Compare GLM and deep neural networks - try out deep learning on some real neural data. See e.g.:
	* [Deep convolutional models improve predictions of macaque V1 responses to natural images](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006897).
	* [Multilayer Recurrent Network Models of Primate Retinal Ganglion Cell Responses](https://openreview.net/forum?id=HkEI22jeg).

A recent paper argued that “modern machine learning” outperforms GLMs in many cases (although in the detailed results shown, GLM outperforms a deep neural network on most of the examples considered). Download their datasets and see if you can do better:
* [Paper](https://www.frontiersin.org/articles/10.3389/fncom.2018.00056/full)
* [Data](https://github.com/KordingLab/spykesML/tree/master/data)

(There are a lot of possible ways to think about improving: the paper did not consider different nonlinearities and made only limited attempts to select GLM features). 

## Jacob Yates

## Carsen Stringer

## Lea Duncker

## James Fitzgerald

## John Serences

Use a continuous time recurrent neural network (example code in python tutorials) to build a network that performs a simple delayed match to sample (DMTS) task (or some other task of your own design). Does the network naturally exhibit within-trial dynamics after training? Does it settle into a crystalized state after reaching asymptotic performance, or does it continue to explore the solution space? What role do these dynamics play in successfully learning your task? And last, what parameters drive increased dynamics in the networks in the support of more efficient processing? For example, in a DMTS memory task, you could look at how the network adaptively prepares to compare the second stimulus to the first during the delay period and what factors might encourage the network to become more dynamic in support of more efficient task performance (e.g. manipulations of the loss function, changes in connectivity, E/I balance, etc)? 

## Jorge Otero-Millan

## Stefan Treue

## Kohitij Kar

## Emily Cooper

I’ve shared a (non-exhaustive) list of some public databases of natural images, depth maps, and eye movements that may be useful for projects [here](https://docs.google.com/document/d/1bVTdvXXoGN4Ya4mutdEBQOQdmO6tc68uHHIccrvdlTI/edit?tab=t.0). Some suggestions:

1. How does the task affect your gaze? Use the [Nymeria Dataset](https://www.projectaria.com/datasets/nymeria/) and/or [Nymeria Gaze Tools](https://github.com/eacooper/NymeriaGazeTools) to extract and quantify patterns in gaze across two different tasks. The Nymeria Dataset contains egocentric video and gaze data recorded from participants performing a variety of naturalistic tasks in real-world environments, and the Nymeria Gaze Tools provide utilities for loading and processing this data. Begin by identifying at least two task categories that are well-represented in the dataset and meaningfully different in their cognitive or motor demands (e.g., navigation vs. object manipulation, or social interaction vs. solitary activity). For each task category, extract and compare gaze-relevant measures of your choosing. Some natural starting points are: fixation duration and spatial dispersion of fixations across the scene. For each measure, compare distributions across task conditions, visualize the results, and apply appropriate statistical tests. Are any of these measures reliably different across tasks? If so, do the differences make intuitive sense given what each task requires of the observer? As an optional extension, ask whether gaze features alone are sufficient to classify the task being performed: this turns your analysis into a prediction problem.

2. What does your next fixation point look like? Using the DOVES dataset of eye movements during free-viewing of calibrated natural images (see [here](https://live.ece.utexas.edu/research/doves/)), select pairs of fixation points in temporal sequence and create small image patches centered on those fixation points. Characterize the visual similarity (or dissimilarity) of these pairs of sequentially fixated image patches using any approaches you’d like (e.g., mutual information, difference in slope of Fourier power spectrum, difference in orientation spectrum, difference in RMS contrast, SSIM). Next, compare the distribution of these measures to a distribution derived from randomly selected pairs of image patches. Are sequentially fixated image patches more similar or different from random pairs of image patches based on any of these measures? Be sure to control for the distance between pairs (image patches that are closer to each other are known to be more similar). If you do find a pattern, does it extend to fixated points with larger separations in time? You could try this analysis on one of the other eye movements datasets, but keep in mind that the pixel intensity values in Hollywood movies are not necessarily linear with respect to light in the world.

3. How far away is your next fixation? When engaged in natural tasks, people tend to fixate points that are relatively close to them, as compared to a random sample of points from their surrounding environment. Using the UT Austin Natural Image Databases (see [here](https://natural-scenes.cps.utexas.edu/db.shtml) – just the subset with co-registered images and depth maps, scroll down to “Stereo Image and Range Data Collection”), investigate potential low level fixation strategies that might recapitulate this behavior. First, simulate a set of random fixation points and plot the distribution of associated scene distances from the depth maps – this should generally match the overall distribution of distances found in the scenes. Next, try biasing your fixation points based on low level properties of the co-registered images run the scene images. For example, you could run the images through an edge detection algorithm and select a random sample of points that fall on luminance edges. You could calculate the local RMS contrast of points and weight your fixation sampling strategy towards higher contrast image regions. You could even assert that people only fixate points that are red. Do any of these strategies result in the near-distance bias we observe in natural fixations?


## Madineh Sedigh-Sarvestani

## Agostina Palmigiano

## Lindsey Glickfeld

In [Barbera et al.](https://www.sciencedirect.com/science/article/pii/S0896627321007856), we used a simple subunit based, Hubel and Wiesel style model to predict V1 responses to gratings and plaids, and then to test the effect of mask phase on these responses. 

1.  This model built V1 cells that only have one (excitatory) subunit and orientation preference/selectivity is defined by the elongation of the long axis of the RF. However, V1 neurons typically have an "on" and an "off" subunit, and in the mouse orientation preference/selectivity is defined by the axis of overlap of these subunits. Build a new version of this model with on/off subunits and test whether this changes (A) the magnitude of cross orientation interactions and (B) the sensitivity of those interactions to mask phase.

2.  In cat/primate V1, plaid stimuli drive responses that are component selective.  However, in mouse V1, responses can be either pattern and component selective. Use this simple subunit model to (A) determine whether V1 neurons are component and/or pattern selective and (B) test whether these responses are sensitive to mask phase. 

The code for the model in Barbera et al. can be found <a href="https://doi.org/10.6084/m9.figshare.c.5677225">here</a>, see _Figure4_model_code.m_.

## Emma Alexander

## Taraz Lee

## Danique Jeurissen

## Geoff Boynton

## Jim DiCarlo

