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

Metamers: given a model and a reference image, stochastically generate a new image whose model representation is identical to that of the reference image.  [ref:  Freeman & Simoncelli 2011]

Eigendistortions: given a model and a reference image, compute the image perturbation that produces the smallest and largest changes (in terms of Euclidean distance) in the model response space.  [ref: Berardino et al 2017]

Maximal differentiation (MAD) competition: given two models that measure distance between images and a reference image, generate pairs of images that optimally distinguish the models. Specifically, synthesize a pair of images that the first model says are equi-distant from the reference while the second model says they are maximally/minimally distant from the reference. Synthesize a second pair with the roles of the two models reversed.  [ref: Wang & Simoncelli 2008]

Geodesics: given a model and two images, attempt to synthesize a sequence of images that lie on the shortest ("geodesic") path in the model's representation space. [ref. Henaff & Simoncelli 2016]

(note from Dan: not really a project idea, but a tool you could use in a project)
My lab has produced a python library of tools to explore vision models by  synthesizing novel informative images.
This includes Metamers (as per my talk yesterday), Eigendistortions (Berardino 2017), Maximal differentiation (MAD) competition (Wang 2008), and Geodesics (Henaff 2016). Might be useful for some students in the course.  If you want to link it from Slack or from the course GitHub, it’s here: https://github.com/LabForComputationalVision/plenoptic/. Kate Bonnen is an expert user and someone to ask questions about it.

## Kate Bonnen

1. Continuous matching experiment.  Employing a tracking method to continuously match a visual feature (e.g., orientation).
2. Continuous subjective measurements.  Measuring subjective signals (e.g., target detection in noise — what is your confidence that you can see the target?).
3. Using a sampling approach to fit a Kalman filter with varying parameters (i.e. what if the detectability of the stimulus changes over time).
4. Implement a LQG with subjective beliefs (as in this paper) and then try to design a set of conditions that will maximally expose subjective beliefs about the dynamics of the trajectory.

### Suggestions related to Eero's plenoptic code repository

**From Billy**
I've been wanting to extend metamers to generate several metamers at once that are as maximally different (in either pixel space, model space, or by some other metric) from each other as possible

**From Nikhil**
One thing that could be interesting is to use MAD competition to generate images that can differentiate between deepnet layers and the portilla model. People have done a lot just synthesizing from both models but could be interesting to see if there are actual fundamental differences in the representations that are captured by each.
In the same vain, I'd like to see how well the portilla model does at discriminative tasks like classification. Since a lot of work is saying deepnets trained for classification are texture biased it would be interesting to just see how well a texture model does at object recognition for example on imagenet. Maybe it can provide a better baseline to then evaluate performance of recognition models that capture more than just texture statistics.

**From Pierre-Étienne**
It would be interesting to use eigendistortions to understand the computational role of layers deep inside a network (/biological system). Instead of end2end maximally minimally visible distortions, one could ask for changes in an image that result in changes of the representation in layer i that is most / least visible to layer j. Same question could be asked of unit i and unit j. Same question can be asked for the curvature of sequences (geodesics), which would help understand what piece in a net do straightening and how.
An idea to help understand the shape of the natural image manifold is to use triplets of related images and a model to measure the angles between the geodesics that link them, the shapes of these triangles would reveal the local curvature of the space as seen by the model.
A texture aware (full reference) perceptual metric would compare isolated features accurately (allowing for shifts and changes in luminance/contrast) while comparing textures loosely (using local statistics only)- and gradually interpolate between these two extremes. A step in that direction is to build a normalized steerable pyramid distance (an evolution of the normalized laplacian pyramid) with a texture/feature gate given by the ratio of local representation std to local representation mean. One would then show that the metric is tolerant to resamplings of texture patterns and sensitive to the exact form of isolated features, just like our visual experience (ie do psychophysics).

**From Xinyuan Zhao**
There is a perceptual distance metric called normalized steerable pyramid distance (NSPD) in the code. It is analogous to the published work of normalized Laplacian pyramid distance (NLPD), only replacing the Laplacian pyramid with the steerable pyramid. I have spent some time working on it, but did not get it to perform very well (now about the same as NLPD). Maybe it can be improved by summer school students.


## Anitha Pasupathy

In Kim et al., 2019, we demonstrated that shape selectivity in V4 is independent of texture selectivity. In other words, selectivity for 2D shape is similar regardless of the surface texture that's painted on the shape. This argues against the possibility that shape selectivity is a by-product of preference for higher order texture statistics in V4 (Okazawa et al., 2013).

Using the artiphysiology approach of Pospisil et al., (2018) one could ask whether individual units in AlexNet (or another DNN) exhibit the same shape preference across different surface textures painted on the 2D shape.  Comparing the circuitry of units that show texture-invariant shape selectivity and those that do not, one could get some insights into how texture-invariant shape selectivity might be built.

(Note from Dan: see [roboflow](https://models.roboflow.com/) for some pre-trained PyTorch models to run)

## Johannes Burge

1) Code up AMA-Gauss (Jaini & Burge, 2017) in PyTorch. 
Step 1: Write code that takes i) a labeled training set of stimuli, ii) an arbitrary set of filters (receptive fields), iii) defines a filter response model, and iv) uses the responses to each stimulus to compute a posterior probability distribution over the latent variable. This is the key computation.
Step 2: Write code that computes a cost from the posterior probability distribution (e.g. L0 norm, L2 norm, KL divergence, etc.)… see the attached suppelmentary texts S4-S6 from Burge & Jaini (2017). PLoS CB.
Step 3: Write code that optimizes the filters to minimize the cost function. 

2) Code up the full version of AMA  in PyTorch (see Burge & Jaini, 2017)… much harder... 

3) Code up either AMA-Gauss or the full version of AMA where the recovered filters (i.e. receptive fields) are constrained to be within a particular family of filters (e.g. Gabors).

Accuracy Maximization Analysis (AMA) is a recently developed Bayesian ideal observer method for task-specific dimensionality reduction. It allows one to automatically determine the stimulus features that are most useful for performing a sensory-perceptual task of scientific interest. This tool is particularly useful for determining how to construct image-computable ideal observer models (i.e. images in, optimal estimates out) for tasks with natural signals (see Burge, 2020 for review). 

AMA has currently been implemented only in matlab (see link to GitHub page). Matlab, generally speaking, does not take advantage of many modern advances in model-parameter optimization. PyTorch does.

The modern methods that PyTorch makes accessible should dramatically improve the practical utility of AMA by helping it avoid local minima and more quickly finding global minima, especially as problem sizes increase in scope. 

Notes:
Kate Bonnen has offered to provide PyTorch-specific technical support in case somebody needs it. And I can provide project-specific know-how to anyone who needs help w. target-tracking related projects (see Kate’s email from last night). 

## Jennifer Groh

"How does a brain create/read out a multiplexed code?  Figure 7 of Caruso et al 2018 provides a back-of-the-envelope sketch of a circuit model of some possibilities for the de-multiplexing.  Try implementing one of these, or come up with your own! "

## Jenny Read

**Analysis of eye tracking data of faces with cleft lip**

A group of cleft lip and palate surgeons are interested in developing better metrics of repair quality. As an initial project, we have collected eye tracking data of \~70 participants viewing 24 photos, 3 photos of 8 patients showing their face pre-op, immediately post-op and some years post-op. The participants include lay people and cleft professionals. The photos have been marked up into 20 anatomical regions of interest (ROIs). We are trying to figure out good metrics to describe patterns of eye movements, e.g. % time fixating a given ROI, or the matrix of transition probabilities between ROIs. If a student is interested in working with this dataset to try out these or their own ideas, we can supply it.

**Modelling sensitivity to stereoscopic depth information in space and time**

Kane et al (attached) examined the minimum (ie threshold) and maximum perceivable disparity for depth corrugations of different spatial and temporal frequencies, and concluded that they were well described by windowed cross-correlation within separable spatial and temporal windows (Rogers & Bradshaw, attached). In their stimuli, the depth corrugations were all horizontally oriented. Thus, they could not examine the well-known stereo anisotropy, whereby at low spatial frequencies disparity thresholds are lower (ie stereoacuity is better) for horizontally-oriented depth corrugations compared to vertical. My collaborator Prof Ignacio Serrano-Pedraza at Universidad Complutense de Madrid has collected disparity thresholds for both horizontal and vertical disparity gratings as a function of spatial and temporal frequency. In this project, you will reproduce the methods of Kane et al but with an anisotropic spatial window, i.e. allowing the window to extend further horizontally than vertically. You will fit this model to Prof Serrano-Pedraza’s dataset in order to assess whether this generalisation can account simultaneously for thresholds to gratings of both orientations. 

## Josh Gold

Use a task like the one here (https://elifesciences.org/articles/73610) to find the limits, in terms of number of objects and length of time they need to be stored, at which individual items are no longer stored in visual memory individually and instead are aggregated into a decision variable.

Use the information-bottleneck (https://openresearchsoftware.metajnl.com/articles/10.5334/jors.322/) to show how real or simulated behavioral data from a 2AFC task can reflect similar overall performance (e.g., measured as % correct) but radically different decision strategies that range from the relatively effective use of a restricted subset of task-relevant stimuli to the relatively ineffective use of all task-relevant stimuili.

## Tatiana Engel

**Representational geometry of visual stimuli across the mouse brain during IBL task**

International Brain Laboratory (IBL) is a large-scale collaboration which aims to understand brain-wide computations underlying complex behavior. IBL records neural activity from all areas of the mouse brain with Neuropixels probes while mice perform a two-alternative forced-choice visual discrimination task. On each trial, a visual grating stimulus appears on the right or left side of the screen, and the mouse needs to turn a wheel to bring the stimulus to the screen center. The task has a hidden block structure. In a left block, the stimuli are more likely to appear on the left. In a right block, they are more likely to appear on the right. The blocks switch stochastically without an explicit cue provided to the mouse. The mouse needs to discriminate left and right stimuli, and also it needs to incorporate the block prior information to perform the task optimally. Details of the task and mouse behavior are described in https://elifesciences.org/articles/63711.

Neural activity across many brain regions changes in response to different task variables. The task variables include the location of the visual stimulus (left vs. right), stimulus contrast, the current block, and the animal’s choice on each trial. Mouse behavior indicates that mice use block prior information to guide their choices. We may, therefore, expect that representations of visual stimuli change depending on the block. The representation of stimuli may also differ between correct and error trials. In addition, we expect that the representations of visual stimuli differ across brain areas. Early sensory areas may carry a more veridical representation of stimuli, whereas association and motor areas may represent stimuli in a more categorical way reflecting the binary choice.

The project can use the representational geometry tools to explore how representations of visual stimuli depend on the block and choice and how they differ across brain regions. For example, for each combination of block and choice, you can compute the representational dissimilarity matrix (RDM) for visual stimuli (for each contrast level on each left and right side) using neural activity in several brain region. You can compare these RDMs across conditions and brain areas. Do we see a block structure in RDM indicating a categorical representation? Do we see that on error trials the stimulus representations collapse (distances shrink) leading to poor discriminability?

 * You can experiment with different definitions of distances, such as a simple Euclidian distance based just on the mean trial-average firing rates versus Mahalonobis distance that takes the noise covariance matrix into account. You can experiment with using the square-root transform (variance stabilizing transform) that makes noise more Gaussian-like (suitable for Mahalonobis distance). You can find technical details about computing distances in this review paper: https://www.nature.com/articles/s41583-021-00502-3.
 * You can also visualize the manifold of neural responses using the multidimensional scaling algorithm.
 * You can explore the tuning properties of neurons that are used to compute RDMs. Can you find lawful relationship between tuning curves properties and RDMs?

You can download the IBL dataset here: https://int-brain-lab.github.io/iblenv/notebooks_external/data_release_repro_ephys.html