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

## Jacob Yates

## Carsen Stringer

## Lea Duncker

## James Fitzgerald

## John Serences

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

## Emma Alexander

## Taraz Lee

## Danique Jeurissen

## Geoff Boynton

## Jim DiCarlo

