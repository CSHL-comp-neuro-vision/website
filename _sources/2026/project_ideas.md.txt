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

Here are two colab notebooks that work as tutorials for modeling and measuring neural selectivity during natural vision. The datasets that accompany them should automatically download when run.
* [shifter](https://drive.google.com/file/d/1IWwcktZbyNruXmU5QbPIOYAIRg2JqqrT/view?usp=drive_link)
* [modeling](https://drive.google.com/file/d/1vyh5Lz-75bJo6f5hNzsFOuN5UNW43Hu5/view?usp=drive_link)

One project could be to try to add inductive biases based on known properties of the visual front end to improve the modeling in the second notebook. Does adding a retina improve the generalization across stimulus domains? 

## Carsen Stringer

In [Du et al 2025](https://www.nature.com/articles/s41467-025-61171-9), we recorded a new dataset of over 29,000 neurons responding to up to 65,000 natural image presentations in mouse V1. These neurons were expressing jGCaMP8s and we recorded their activity using two-photon calcium imaging at a rate of 30Hz. We fit simplified two-layer convolutional neural network models to each neuron, explaining around 70% of the response variance in the dataset. We have an example tutorial on how to fit linear and two-layer convolutional models to this dataset [here](https://github.com/MouseLand/course-materials/tree/main/visual_models), and the full dataset is available [here](https://janelia.figshare.com/articles/dataset/Towards_a_simplified_model_of_primary_visual_cortex/28797638). 

Example projects include exploring how downstream circuits in the mouse brain may extract features from the visual world, by using these simplified models as input to a larger model and training the model to perform a task such as object recognition or object tracking. The students can also explore alternative architectures for the neural responses, using a variety of pretrained CNN or transformer models, such as from huggingface, as a base for fitting the visual responses in the dataset. Another option is to explore the features that the neurons are most selective for, and looking for patterns across neurons based on receptive field location or size.

## Lea Duncker

## James Fitzgerald

In my talk, I will discuss behavior, neural coding, and network mechanisms associated with visual motion processing. I will primarily emphasize flies and zebrafish for the mechanistic possibilities afforded by connectomics and whole-brain functional imaging. I encourage interested students to reach out to me for more information and discussion.

1. Neural network mechanisms of binocular integration in larval zebrafish. We recently developed a theoretical framework for predicting synaptic connectivity from densely measured neuronal activity, and we are now applying this theory to a Function-Linked (FuL) Connectomics collected by the Baier lab at the Max Planck Institute for Biological Intelligence. More specifically, the dataset consists of functional calcium imaging of optic-flow-responsive neurons in the pretectum and electron-microscopy based connectomics in the same specimen. The pretectum is a retinorecipient brain area, but retinal responses were not measured experimentally. This project would examine the impact that various retinal models have on the predictions of the theory. References: [1](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.4.023255), [2](https://arxiv.org/abs/2310.20309), [3](https://www.nature.com/articles/s41592-022-01621-0).
2. Behaviorally aligned representations in larval zebrafish. We recently found that the statistics of behavior predict the statistics of visual motion encoding in many regions of the zebrafish brain. This project would examine how decisions made when quantifying behavior impact the model's predictions and explanatory power. For instance, what behavioral quantification works best to explain the data in pretectum and other visual areas? Do the statistics of measured behavior or descending motor commands better predict visual activity? References:[1](https://www.biorxiv.org/content/10.64898/2026.02.04.703828v2.abstract), [2](https://www.cell.com/current-biology/fulltext/S0960-9822(25)01003-6).
3. From connectomics to algorithm. I have long-standing interests in the algorithms of visual motion estimation and their normative basis in natural scene statistics. Most recently, I have been building connectome-constrained models. This project would explore ways to connect these two aspects of my research interests in the fly. References: [1](https://www.annualreviews.org/content/journals/10.1146/annurev-vision-101623-025432), [2](https://www.biorxiv.org/content/10.1101/2024.11.01.621596v2.abstract)

## John Serences

Use a continuous time recurrent neural network (example code in python tutorials) to build a network that performs a simple delayed match to sample (DMTS) task (or some other task of your own design). Does the network naturally exhibit within-trial dynamics after training? Does it settle into a crystalized state after reaching asymptotic performance, or does it continue to explore the solution space? What role do these dynamics play in successfully learning your task? And last, what parameters drive increased dynamics in the networks in the support of more efficient processing? For example, in a DMTS memory task, you could look at how the network adaptively prepares to compare the second stimulus to the first during the delay period and what factors might encourage the network to become more dynamic in support of more efficient task performance (e.g. manipulations of the loss function, changes in connectivity, E/I balance, etc)? 

## Jorge Otero-Millan

1. Saccade control and plant compensation

Derive (or learn) the optimal control policy for a saccade when the oculomotor plant is a first-order low-pass, with viscosity and an elastic restoring force but inertia neglected. Start by inverting the plant to confirm the classic result analytically: a step proportional to position plus a pulse proportional to velocity. Then ask whether an optimization or a trained policy recovers it. Solve the minimum-time problem with bounded drive by Pontryagin's principle (the answer is a single rectangular pulse, one switch, then a tonic step), and compare against minimizing control effort or endpoint variance under signal-dependent noise, which you can do analytically or with policy-gradient learning through the differentiable plant.

2. Sensor fusion for gaze stabilization

Derive (or learn) how to fuse visual and vestibular signals for gaze stabilization, where the goal is to compensate for sensor dynamics. The two sensors are complementary: the semicircular canals report head angular velocity through a high-pass filter (the cupula's dominant time constant is only a few seconds, so the signal washes out during sustained rotation), while retinal-slip/optokinetic motion is a low-pass, delayed sensor, reliable for steady motion, useless at high frequencies. Start by showing analytically that no single sensor suffices and, crucially, that the brain cannot simply invert the canal: a naive inverse amplifies low-frequency noise without bound, so the well-posed solution is a complementary filter that recovers the missing low-frequency content from vision instead of from inversion. Then ask whether an optimal estimator or a trained policy recovers it: the steady-state Kalman filter that fuses a high-pass, noisy canal measurement with a low-pass, noisy visual measurement of retinal slip is a complementary filter, with a crossover frequency set by the sensor time constants and the noise ratio. Pose the objective as minimizing retinal slip across the frequency bands. Work on velocity no need to model eye position.

## Stefan Treue

## Kohitij Kar

## Emily Cooper

I’ve shared a (non-exhaustive) list of some public databases of natural images, depth maps, and eye movements that may be useful for projects [here](https://docs.google.com/document/d/1bVTdvXXoGN4Ya4mutdEBQOQdmO6tc68uHHIccrvdlTI/edit?tab=t.0). Some suggestions:

1. How does the task affect your gaze? Use the [Nymeria Dataset](https://www.projectaria.com/datasets/nymeria/) and/or [Nymeria Gaze Tools](https://github.com/eacooper/NymeriaGazeTools) to extract and quantify patterns in gaze across two different tasks. The Nymeria Dataset contains egocentric video and gaze data recorded from participants performing a variety of naturalistic tasks in real-world environments, and the Nymeria Gaze Tools provide utilities for loading and processing this data. Begin by identifying at least two task categories that are well-represented in the dataset and meaningfully different in their cognitive or motor demands (e.g., navigation vs. object manipulation, or social interaction vs. solitary activity). For each task category, extract and compare gaze-relevant measures of your choosing. Some natural starting points are: fixation duration and spatial dispersion of fixations across the scene. For each measure, compare distributions across task conditions, visualize the results, and apply appropriate statistical tests. Are any of these measures reliably different across tasks? If so, do the differences make intuitive sense given what each task requires of the observer? As an optional extension, ask whether gaze features alone are sufficient to classify the task being performed: this turns your analysis into a prediction problem.

2. What does your next fixation point look like? Using the DOVES dataset of eye movements during free-viewing of calibrated natural images (see [here](https://live.ece.utexas.edu/research/doves/)), select pairs of fixation points in temporal sequence and create small image patches centered on those fixation points. Characterize the visual similarity (or dissimilarity) of these pairs of sequentially fixated image patches using any approaches you’d like (e.g., mutual information, difference in slope of Fourier power spectrum, difference in orientation spectrum, difference in RMS contrast, SSIM). Next, compare the distribution of these measures to a distribution derived from randomly selected pairs of image patches. Are sequentially fixated image patches more similar or different from random pairs of image patches based on any of these measures? Be sure to control for the distance between pairs (image patches that are closer to each other are known to be more similar). If you do find a pattern, does it extend to fixated points with larger separations in time? You could try this analysis on one of the other eye movements datasets, but keep in mind that the pixel intensity values in Hollywood movies are not necessarily linear with respect to light in the world.

3. How far away is your next fixation? When engaged in natural tasks, people tend to fixate points that are relatively close to them, as compared to a random sample of points from their surrounding environment. Using the UT Austin Natural Image Databases (see [here](https://natural-scenes.cps.utexas.edu/db.shtml) – just the subset with co-registered images and depth maps, scroll down to “Stereo Image and Range Data Collection”), investigate potential low level fixation strategies that might recapitulate this behavior. First, simulate a set of random fixation points and plot the distribution of associated scene distances from the depth maps – this should generally match the overall distribution of distances found in the scenes. Next, try biasing your fixation points based on low level properties of the co-registered images run the scene images. For example, you could run the images through an edge detection algorithm and select a random sample of points that fall on luminance edges. You could calculate the local RMS contrast of points and weight your fixation sampling strategy towards higher contrast image regions. You could even assert that people only fixate points that are red. Do any of these strategies result in the near-distance bias we observe in natural fixations?


## Madineh Sedigh-Sarvestani

The brain, and the visual systems in particular, exhibits a lot of large-scale organization. Where does this organization come from and why is it different among species? One possibility is self-organization, where small-scale local interactions in neural circuits combine to generate large-scale organization, without any explicit ‘training’. Self-organization can be modeled with simple learning rules, or with more complex self-supervised approaches developed recently <a href="https://github.com/CSHL-comp-neuro-vision/slides-2026/raw/main/sedigh-sarvestani/KonkleAlvarez-2022-ASelfSupervisedDomainGeneralLearningFrameworkForHumanVentralStreamRepresentation.pdf">(Konkle and Alvarez 2022)</a>. And it can be used to explain the formation of cortical maps <a href="https://github.com/CSHL-comp-neuro-vision/slides-2026/raw/main/sedigh-sarvestani/Sedigh-Sarvestanietal.-2021-ASinusoidalTransformationOfTheVisualFieldIsTheBasisForPeriodicMapsInAreaV2.pdf">(Sedigh-Sarvestani et al. 2021)</a>, layout of cells in the retina <a href="https://github.com/CSHL-comp-neuro-vision/slides-2026/raw/main/sedigh-sarvestani/ClippingdaleWilson-1996-Self-SimilarNeuralNetworksBasedOnAKohonenLearningRule.pdf">(Clippingdale and Wilson 1996)</a>, place and grid cells and other cases of large-scale neural network organization. What’s more, self-organization in the sensory system can be explained as a natural byproduct of sensorimotor interactions. In other words, the influence of body movements on sensory  inputs may be the critical variable that shapes self-organizing mechanisms in a species-specific way.

To start to play with these ideas. You can read <a href="https://github.com/CSHL-comp-neuro-vision/slides-2026/raw/main/sedigh-sarvestani/ClippingdaleWilson-1996-Self-SimilarNeuralNetworksBasedOnAKohonenLearningRule.pdf">Clippingdale and Wilson 1996</a>,where a simple self-organizing learning rule is used to determine the layout of photoreceptors on the retina, given particular patterns of eye movements. Some starter code is in this google collab <a href="https://colab.research.google.com/drive/1DzVJdCVg4JdkI6_jxf3fFHiMqmETZjNa#scrollTo=UPnARMbeBMcT">notebook</a>. What sort of retinal layouts (e.g. uniform, fovea, etc) develop from a combination of different movement patterns (e.g. rotation and translation in different amounts). You can also try to look up, or simulate, the actual movement distributions for humans (Gaze in Wild and/or GENUA PESTO) and see if the model produces foveal layout. You can then use the code <a href="https://colab.research.google.com/drive/1SH1Moj0KsM-7CluSWZerGco7jtna3QgT">here</a>, to determine if different retinal layouts produce different retinotopy maps in visual areas. You might also try making a hierarchical visual system and feed the retinotopy map of a lower area into a higher one to see how they transform.

You can also invert this exercise. Given a large-scale organization in the visual system, say foveal layout of photoreceptors in the retina, what should eye movements look like? The optimal movement might be defined as one that makes prediction of self-generated sensory inputs easier. In technical jargon, a good motor action is one that produces self-similar sensory inputs. See if you can use this idea to extract the movement distributions above from the retinal layouts produced given the movement distribution.

## Agostina Palmigiano

## Lindsey Glickfeld

In [Barbera et al.](https://www.sciencedirect.com/science/article/pii/S0896627321007856), we used a simple subunit based, Hubel and Wiesel style model to predict V1 responses to gratings and plaids, and then to test the effect of mask phase on these responses. 

1.  This model built V1 cells that only have one (excitatory) subunit and orientation preference/selectivity is defined by the elongation of the long axis of the RF. However, V1 neurons typically have an "on" and an "off" subunit, and in the mouse orientation preference/selectivity is defined by the axis of overlap of these subunits. Build a new version of this model with on/off subunits and test whether this changes (A) the magnitude of cross orientation interactions and (B) the sensitivity of those interactions to mask phase.

2.  In cat/primate V1, plaid stimuli drive responses that are component selective.  However, in mouse V1, responses can be either pattern and component selective. Use this simple subunit model to (A) determine whether V1 neurons are component and/or pattern selective and (B) test whether these responses are sensitive to mask phase. 

The code for the model in Barbera et al. can be found <a href="https://doi.org/10.6084/m9.figshare.c.5677225">here</a>, see _Figure4_model_code.m_.

## Emma Alexander

 Light fields describe the spatial and angular distribution of light, characterizing the set of images that could be taken of a given scene. Thus, light field cameras allow post-capture sampling of images from hypothetical cameras with different positions or apertures. Using light field data such as <a href="https://drive.google.com/file/d/18GiXf3dBND5ZCgKm49AwW7rt0UgV4JV4/view">example 1</a>, <a href="https://drive.google.com/file/d/18GiXf3dBND5ZCgKm49AwW7rt0UgV4JV4/view">example 2</a>, or other light fields available online, we can explore the implications of different optical designs on downstream processing.

Warm up: Use the camera data to extract pinhole images from different viewpoints. Compare pinhole images to full-aperture images in terms of appearance, depth of field, and noise level. Explore spatial-angular slices (sometimes called “epipolar images”). Consider which sub-images would be best for stereo depth perception and depth from defocus, and test these hypotheses.

Project 1: Based on Liang, Chia-Kai, Yi-Chang Shih, and Homer H. Chen. "Light field analysis for modeling image formation." IEEE Transactions on Image Processing, model the light field sampling of an eye of your choice, in the style of fig 1 of Levin, Anat, William T. Freeman, and Frédo Durand. "Understanding camera trade-offs through a Bayesian analysis of light field projections." 

Project 2 Read Banks, Martin S., et al. "Why do animal eyes have pupils of different shapes?." Science Advances. Test the effect of pupil shape on stereo depth performance by simulating apertures from the light field data. Consider what makes a fair comparison and how the effects you observe might be exaggerated through optical design.

Project 3: Read Levin, Anat, et al. "Image and depth from a conventional camera with a coded aperture." ACM transactions on graphics (TOG). Simulate their aperture code and depth recovery algorithm, and compare to non-coded depth from defocus.

## Taraz Lee

You may want to look at saccade adaptation or population receptive field mapping. I believe there are several open PRF mapping data, such as the NYU data set: https://doi-org.proxy.lib.umich.edu/10.1016/j.neuroimage.2021.118609 or something from Kendrick Kay: https://kendrickkay.net/analyzePRF/. It could be fun to try out different parameters for the receptive fields (e.g., 2d gaussian vs mexican hat vs. something else).

## Danique Jeurissen

## Geoff Boynton

<a href="https://github.com/CSHL-comp-neuro-vision/slides-2026/raw/main/boynton/realtime_log_warp_camera.py">realtime_log_warp_camera.py</a>
<a href="https://github.com/CSHL-comp-neuro-vision/slides-2026/raw/main/boynton/realtime_schwartz_v1_warp_camera.py">realtime_schwartz_v1_warp_camera.py</a>

1. Modify the ‘Schwartz’ V1 mapping code to add V2 and V3 retinotopic maps, like those in:  https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000651
2. Modify the ‘Schwartz’ V1 script to incorporate the individual differences seen in Duncan et al (2003).  Can you perceive the differences in the cortical magnification when showing a standard image like an eye-chart?
3. Add an artificial scotoma in the mapping.  How does the apparent size and shape of a lesion depend on whether it is defined in visual or cortical coordinates?
4. Simulate microsaccades and small eye movements.  How does this affect the location of positions in the fovea representation of V1 compared to the periphery?

## Jim DiCarlo

