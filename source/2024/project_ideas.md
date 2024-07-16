# Project Ideas

## EJ Chichilnisky

Explore the evolution of computational models for light responses in the retina and think about how to evaluate their performance and what they teach us about visual processing.

Start by downloading the data set from [Pillow et al GLM paper (2008)](https://github.com/CSHL-comp-neuro-vision/tutorials/tree/main/data/Pillow-2008):

* fit a LN model to the data (see [this paper](https://pubmed.ncbi.nlm.nih.gov/11405422)) 
* fit a GLM to the data (see [this paper](http://www.ncbi.nlm.nih.gov/pubmed/18650810))
* fit a “subunit” model to the data (see [this paper](https://www.ncbi.nlm.nih.gov/pubmed/32149600))
* fit a CNN model to the data (see [this paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5515384))

The first and second models will be fairly easy based on the code provided and what you learned in the lecture today.
The third and fourth will involve digging in to newer models and working with this data set.

Questions:
* What is the best metric by which to assess model performance?
* How much more accurately do the more complex models perform?
* What do these different models tell you about the retinal computations?
* What are the limitations of the stimulus (rather than the model) in this setting?
* What are the challenges of producing predicted spike trains from these models?
* BONUS: Clean up this distribution and provide Python access code!
* BONUS: Provide code for the last two models to include in this distribution!

## John Serences

Use a continuous time recurrent neural network (example code in python tutorials) to build a network that performs a simple delayed match to sample (DMTS) task (or some other task of your own design). Does the network naturally exhibit within-trial dynamics after training? Does it settle into a crystalized state after reaching asymptotic performance, or does it continue to explore the solution space? What role do these dynamics play in successfully learning your task? And last, what parameters drive increased dynamics in the networks in the support of more efficient processing? For example, in a DMTS memory task, you could look at how the network adaptively prepares to compare the second stimulus to the first during the delay period and what factors might encourage the network to become more dynamic in support of more efficient task performance (e.g. manipulations of the loss function, changes in connectivity, E/I balance, etc)? 

## Eero Simoncelli

1. Metamers: given a model and a reference image, stochastically generate a new image whose model representation is identical to that of the reference image.  [ref:  Freeman & Simoncelli 2011]

2. Eigendistortions: given a model and a reference image, compute the image perturbation that produces the smallest and largest changes (in terms of Euclidean distance) in the model response space.  [ref: Berardino et al 2017]

3. Maximal differentiation (MAD) competition: given two models that measure distance between images and a reference image, generate pairs of images that optimally distinguish the models. Specifically, synthesize a pair of images that the first model says are equi-distant from the reference while the second model says they are maximally/minimally distant from the reference. Synthesize a second pair with the roles of the two models reversed.  [ref: Wang & Simoncelli 2008]

4. Geodesics: given a model and two images, attempt to synthesize a sequence of images that lie on the shortest ("geodesic") path in the model's representation space. [ref. Henaff & Simoncelli 2016]

(note from Dan: not really a project idea, but a tool you could use in a project)
My lab has produced a python library of tools to explore vision models by  synthesizing novel informative images.
This includes Metamers (as per my talk yesterday), Eigendistortions (Berardino 2017), Maximal differentiation (MAD) competition (Wang 2008), and Geodesics (Henaff 2016). Might be useful for some students in the course.  If you want to link it from Slack or from the course GitHub, it’s [here]https://github.com/LabForComputationalVision/plenoptic/: Kate Bonnen is an expert user and someone to ask questions about it.

## Stephanie Palmer

Project ideas:
Open the provided natural movie and associated retinal [data](https://github.com/CSHL-comp-neuro-vision/tutorials/blob/main/data/Palmer-2024/salamanderRGCdata_long_fish_movie.mat) from the larval salamander. Use DeepLabCut, your favorite tracking algorithm, or your own hand-tracking to map out the trajectories of 1-5 objects in one of the five scenes. Does the retinal population have information about these trajectories? Compute the correlation between the population firing and the past, present, and future position of your chosen object. At what lag is the correlation maximal? What other metrics could you use to quantify this? 

Try to animate a circle so that it looks "alive". What kind of features do you want your pet circle's trajectory to have? Try making it unpredictable; try making it oscillate. Can you make a trajectory that would pass a Turing test?

Find a good open-source model retina and play it a natural movie. How much can you modify the movie before you can tell the difference in the retina's response. Find the retina's metamers! This riffs on ideas you'll hear from Eero and EJ. 

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

Try loading the DOVES dataset and making a movie out of the eye trajectories. This data (<a href="https://github.com/CSHL-comp-neuro-vision/tutorials/tree/main/matlab/Doves-Yates2024">Matlab</a>/<a href="https://github.com/CSHL-comp-neuro-vision/tutorials/tree/main/python/Doves-Yates2024">Python</a>) contains natural images with dpi eyetracking and is likely useful to many projects.


## Lea Duncker

A scalable Bayesian STRF model through Gaussian Process inducing points

A lot of work in receptive field modeling has been concerned with the development of scalable and data efficient estimators. Here, a common approach has been to encode known receptive field properties like smoothness, locality, or temporal recency in a statistical model of the receptive field weights. Popular choices for this have been the use of a set of basis functions [1] or to do maximum a posteriori estimation and type-II maximum likelihood learning in a Bayesian linear regression model with a given choice of prior distribution [2, 3, 4]. An attractive choice for such prior distributions have been Gaussian Processes [2, 3, 4, 5], where assumptions like smoothness in the receptive field are encoded through the covariance between neighboring weights. While these models are conceptually attractive, they suffer from scalability issues – it’s hard to apply them in settings with large stimulus ensembles. Thus, a lot of work has focused on taking this approach and making estimators scalable, typically by approximating the resulting prior distribution in some way [4, 6].

The idea for this project is to consider the same setting of Bayesian linear regression, where the linear weights are the receptive field and a prior distribution over the weights is modeled as a Gaussian Process. We will use an idea from the Gaussian Process literature called “inducing points” [7] to develop a scalable estimation approach. The project will involve:

• Familiarizing yourself with the literature on GP-based STRF models
• Pen and paper derivations of the model equations
• Implementation of the sparse GP regression building on existing GP libraries in Python (e.g. GPflow or GPytorch)
• Applications to simulated and neural data 

References: 
[1] Pillow, J. W., Shlens, J., Paninski, L., Sher, A., Litke, A. M., Chichilnisky, E. J., & Simoncelli, E. P. (2008). Spatio-temporal correlations and visual signalling in a complete neuronal population. Nature, 454(7207), 995-999.
[2] Sahani, M., & Linden, J. (2002). Evidence optimization techniques for estimating stimulus-response functions. Advances in neural information processing systems, 15.
[3] Park, M., & Pillow, J. W. (2011). Receptive field inference with localized priors. PLoS computational biology, 7(10), e1002219.
[4] Duncker, L., Ruda, K. M., Field, G. D., & Pillow, J. W. (2023). Scalable variational inference for low-rank spatiotemporal receptive fields. Neural computation, 35(6), 995-1027.
[5] Williams, C., & Rasmussen, C. (1995). Gaussian processes for regression. Advances in neural information processing systems, 8.
[6] Aoi, M. C., & Pillow, J. W. (2017). Scalable Bayesian inference for high-dimensional neural receptive fields. bioRxiv, 212217.
[7] Titsias, M. (2009, April). Variational learning of inducing variables in sparse Gaussian processes. In Artificial intelligence and statistics (pp. 567-574). PMLR.

## Ruth Rosenholtz

See also this useful [code repository](https://github.com/RosenholtzLab/CCP_CSHL)!

1. Combining predictions of peripheral vision with fixation data. We provide a subset of 100 images from the COCO-Periph dataset. The visualizations and code provided allow one to create visualizations of the information available for a (mostly) arbitrary fixation. We also provide eye tracking data for these images, from the COCO-Search 18 dataset from Greg Zelinsky. Observers executed these fixations while performing a search task. This combination of model predictions and eye tracking data should enable a number of interesting projects. For instance, consider the sequence of fixation locations, {(fx_i, fy_i), (fx_i+1, fy_i+1)}. Was the object at (fx_i+1, fy_i+1) likely identifiable when fixating (fx_i, fy_i), according to the peripheral vision model? In which case what might be the purpose of that saccade?

2. Many aspects of peripheral vision get worse in a roughly linear way. Acuity worsens as an approximately linear function of eccentricity, as does the critical spacing of crowding, as do hyperacuity and other aspects of vision. Van Essen and Anderson (1995) and others have suggested that this makes the information encoded about a stimulus relatively invariant to viewing distance. Under what circumstances does this hold, and when does it fail? Does it matter that the different linear functions have different slopes and intercepts?

## Rachel Denison

1. Maximally informative time points. We don’t need to pay attention at every moment, because sometimes nothing interesting is happening. Given a movie clip and a task that you specify, build a system that will learn the time points (frames in the movie) that are most informative for completing the task. You can use movies and tasks with varying degrees of complexity, so consider starting as simply as possible and building up from there!

2. Timing a brain process. Many aspects of neural control—including the control of visual attention—involve generating precisely timed brain activity. Build a neural network that delivers an output spike at a specified temporal interval following an input stimulus. Consider trying different timing mechanisms used by the brain, including ramping, oscillations, and trajectories through a state-space. How does the temporal precision of your output spike depend on the length of the interval? If you have solved the problem for one fixed interval, can you build a network that can generate an arbitrary temporal interval? Can you build a network that can learn a new temporal interval?

3. Contending with temporal uncertainty. Sometimes we know approximately when an important event will occur, but we don’t have perfect timing information. Such temporal uncertainty can arise from internal sources, like imprecision in our timing estimates, or external sources, like stochasticity in event times (e.g., a bus that comes approximately every 15 minutes but can be a little early or late). Consider a task in which a single stimulus appears with temporal uncertainty on each trial and the observer has to make some report on it. Given some source of temporal uncertainty that you specify, how should the observer allocate attention over time to maximize task performance across trials? You will need to make some assumptions about 1) how attention can be allocated across time (if there are no constraints, the observer could just attend all the time) and 2) how the amount of attention at the time of the stimulus relates to task performance.

4. On a different note, if you are interested in visual metacognition, the Confidence Database is a great resource of behavioral data with ~150 datasets and counting. There are many possible analysis projects that could be done using <a href="https://osf.io/s46pr/">these data</a> by  <a href="../_static/pdfs/denison/rahnev-et-al-2020-nhb.pdf">Rahnev et al. (2020). The Confidence Database. _Nature Human Behaviour, 4_(3):317-325.</a>

## Tony Movshon

Building a motion energy model for cortical direction selectivity. As a starting point, look at the <a href="https://github.com/CSHL-comp-neuro-vision/tutorials/tree/main/matlab/ModelingMotionProcessing">model in the Rust et al 2006 paper</a> -- motion energy front end, then pattern motion computation. I will talk about that paper at the end of the lecture.

It's a good package and a good exercise for students.


## Kate Bonnen

1. Continuous matching experiment.  Employing a tracking method to continuously match a visual feature (e.g., orientation).

2. Continuous subjective measurements.  Measuring subjective signals (e.g., target detection in noise — what is your confidence that you can see the target?).

3. Using a sampling approach to fit a Kalman filter with varying parameters (i.e. what if the detectability of the stimulus changes over time).

4. Implement a LQG with subjective beliefs (as in this paper) and then try to design a set of conditions that will maximally expose subjective beliefs about the dynamics of the trajectory.

**Suggestions related to Eero's plenoptic code repository**

**From Billy**
1. I've been wanting to extend metamers to generate several metamers at once that are as maximally different (in either pixel space, model space, or by some other metric) from each other as possible

**From Nikhil**
1. One thing that could be interesting is to use MAD competition to generate images that can differentiate between deepnet layers and the portilla model. People have done a lot just synthesizing from both models but could be interesting to see if there are actual fundamental differences in the representations that are captured by each.
2. In the same vain, I'd like to see how well the portilla model does at discriminative tasks like classification. Since a lot of work is saying deepnets trained for classification are texture biased it would be interesting to just see how well a texture model does at object recognition for example on imagenet. Maybe it can provide a better baseline to then evaluate performance of recognition models that capture more than just texture statistics.

**From Pierre-Étienne**
1. It would be interesting to use eigendistortions to understand the computational role of layers deep inside a network (/biological system). Instead of end2end maximally minimally visible distortions, one could ask for changes in an image that result in changes of the representation in layer i that is most / least visible to layer j. Same question could be asked of unit i and unit j. Same question can be asked for the curvature of sequences (geodesics), which would help understand what piece in a net do straightening and how.
2. An idea to help understand the shape of the natural image manifold is to use triplets of related images and a model to measure the angles between the geodesics that link them, the shapes of these triangles would reveal the local curvature of the space as seen by the model. A texture aware (full reference) perceptual metric would compare isolated features accurately (allowing for shifts and changes in luminance/contrast) while comparing textures loosely (using local statistics only)- and gradually interpolate between these two extremes. A step in that direction is to build a normalized steerable pyramid distance (an evolution of the normalized laplacian pyramid) with a texture/feature gate given by the ratio of local representation std to local representation mean. One would then show that the metric is tolerant to resamplings of texture patterns and sensitive to the exact form of isolated features, just like our visual experience (ie do psychophysics).

**From Xinyuan Zhao**
1. There is a perceptual distance metric called normalized steerable pyramid distance (NSPD) in the code. It is analogous to the published work of normalized Laplacian pyramid distance (NLPD), only replacing the Laplacian pyramid with the steerable pyramid. I have spent some time working on it, but did not get it to perform very well (now about the same as NLPD). Maybe it can be improved by summer school students.

## Stefan Treue

## Emily Cooper

I’ve shared a (non-exhaustive) list of some public databases of natural images, depth maps, and eye movements that may be useful for projects <a href="https://docs.google.com/document/d/1bVTdvXXoGN4Ya4mutdEBQOQdmO6tc68uHHIccrvdlTI/edit?usp=sharing">here</a>:

1. What does your next fixation point look like? 
Using the DOVES dataset of eye movements during free-viewing of calibrated natural images (see <a href="https://live.ece.utexas.edu/research/doves/">Google Doc</a>), select pairs of fixation points in temporal sequence and create small image patches centered on those fixation points. Characterize the visual similarity (or dissimilarity) of these pairs of sequentially fixated image patches using any approaches you’d like (e.g., mutual information, difference in slope of Fourier power spectrum, difference in orientation spectrum, difference in RMS contrast, SSIM). Next, compare the distribution of these measures to a distribution derived from randomly selected pairs of image patches. Are sequentially fixated image patches more similar or different from random pairs of image patches based on any of these measures? Be sure to control for the distance between pairs (image patches that are closer to each other are known to be more similar). If you do find a pattern, does it extend to fixated points with larger separations in time? You could try this analysis on one of the other eye movements datasets, but keep in mind that the pixel intensity values in Hollywood movies are not necessarily linear with respect to light in the world.

2. How far away is your next fixation?
When engaged in natural tasks, people tend to fixate points that are relatively close to them, as compared to a random sample of points from their surrounding environment. Using the UT Austin Natural Image Databases (see <a href="https://natural-scenes.cps.utexas.edu/db.shtml">Google Doc</a> – just the subset with co-registered images and depth maps, scroll down to “Stereo Image and Range Data Collection”), investigate potential low level fixation strategies that might recapitulate this behavior. First, simulate a set of random fixation points and plot the distribution of associated scene distances from the depth maps – this should generally match the overall distribution of distances found in the scenes. Next, try biasing your fixation points based on low level properties of the co-registered images run the scene images. For example, you could run the images through an edge detection algorithm and select a random sample of points that fall on luminance edges. You could calculate the local RMS contrast of points and weight your fixation sampling strategy towards higher contrast image regions. You could even assert that people only fixate points that are red. Do any of these strategies result in the near-distance bias we observe in natural fixations?  

## Marlene Cohen

1. Generate a fake multineuron data set. This should include spike count, BOLD, or calcium imaging responses of n neurons (or voxels) on m trials. You could use models from any of several tutorials to generate these responses. (I know that ChoiceProbabilityTutorial will do this for a population of MT neurons.) From this fake data set, calculate:

a. The average correlation between each pair of neurons (this could be noise or signal correlation, depending on the data set you generated).  

b. The dimensionality of the shared variability (e.g. by calculating the proportion variance explained by the first k principal components for k=1:n) 

c. For the overachievers among you, calculate some fancy measurements too, such as communication subspace dimensionality if you modeled multiple brain areas (good code <a href="https://github.com/joao-semedo/communication-subspace">here</a>) or average or modal controllability (good code at #3 <a href="https://complexsystemsupenn.com/codedata">here</a>; start with the correlation matrix with the diagonal set to 0 instead of 1). If you would like to experiment with topological data analysis, I can provide code for that too.  

d. Next, make some change to your model that will affect the shared variability (maybe add in a common noise source, or change some model parameters) and repeat the calculations in #a-c. Can you gain some insight into how those numbers are related? 

e. Possible publishable extension: Do these calculations in a real data set (yours? Or several from my lab are available if you would like). Which ways of quantifying shared variability are most closely associated with behavior, stimuli, task condition, or some other quantity you think is important?

## Madineh Sedigh-Sarvestani

The brain, and the visual systems in particular, exhibits a lot of large-scale organization. Where does this organization come from and why is it different among species? One possibility is self-organization, where small-scale local interactions in neural circuits combine to generate large-scale organization, without any explicit ‘training’. Self-organization can be modeled with simple learning rules, or with more complex self-supervised approaches developed recently <a href="../_static/pdfs/sedigh-sarvestani/KonkleAlvarez-2022-ASelfSupervisedDomainGeneralLearningFrameworkForHumanVentralStreamRepresentation.pdf">(Konkle and Alvarez 2022)</a>. And it can be used to explain the formation of cortical maps <a href="../_static/pdfs/sedigh-sarvestani//Sedigh-Sarvestanietal.-2021-ASinusoidalTransformationOfTheVisualFieldIsTheBasisForPeriodicMapsInAreaV2.pdf">(Sedigh-Sarvestani et al. 2021)</a>, layout of cells in the retina <a href="../_static/pdfs/sedigh-sarvestani/ClippingdaleWilson-1996-Self-SimilarNeuralNetworksBasedOnAKohonenLearningRule.pdf">(Clippingdale and Wilson 1996)</a>, place and grid cells and other cases of large-scale neural network organization. What’s more, self-organization in the sensory system can be explained as a natural byproduct of sensorimotor interactions. In other words, the influence of body movements on sensory  inputs may be the critical variable that shapes self-organizing mechanisms in a species-specific way.

To start to play with these ideas. You can read <a href="../_static/pdfs/sedigh-sarvestani/ClippingdaleWilson-1996-Self-SimilarNeuralNetworksBasedOnAKohonenLearningRule.pdf">Clippingdale and Wilson 1996</a>,where a simple self-organizing learning rule is used to determine the layout of photoreceptors on the retina, given particular patterns of eye movements. Some starter code is in this google collab <a href="https://colab.research.google.com/drive/1DzVJdCVg4JdkI6_jxf3fFHiMqmETZjNa#scrollTo=UPnARMbeBMcT">notebook</a>. What sort of retinal layouts (e.g. uniform, fovea, etc) develop from a combination of different movement patterns (e.g. rotation and translation in different amounts). You can also try to look up, or simulate, the actual movement distributions for humans (Gaze in Wild and/or GENUA PESTO) and see if the model produces foveal layout. You can then use the code <a href="https://colab.research.google.com/drive/1SH1Moj0KsM-7CluSWZerGco7jtna3QgT">here</a>, to determine if different retinal layouts produce different retinotopy maps in visual areas. You might also try making a hierarchical visual system and feed the retinotopy map of a lower area into a higher one to see how they transform.

You can also invert this exercise. Given a large-scale organization in the visual system, say foveal layout of photoreceptors in the retina, what should eye movements look like? The optimal movement might be defined as one that makes prediction of self-generated sensory inputs easier. In technical jargon, a good motor action is one that produces self-similar sensory inputs. See if you can use this idea to extract the movement distributions above from the retinal layouts produced given the movement distribution.


## Ione Fine

• Create a collection of receptive fields (e.g. oriented Gabors that vary in location, orientation and size tuning. How is  a ‘star’ (a light spot in a dark background) represented amongst these Gabors? How would you best represent a ‘star’ with this collection of receptive fields. 
• We see adaptation in cortical electrical stimulation. It may or may not be the same thing as normal cortical adaptation to standard visual stimulation. It might be worth having a think about that. 
• What about an LGN prosthetic?

## Emma Alexander

Light fields describe the spatial and angular distribution of light, characterizing the set of images that could be taken of a given scene. Thus, light field cameras allow post-capture sampling of images from hypothetical cameras with different positions or apertures. Using light field data such as <a href="https://drive.google.com/file/d/18GiXf3dBND5ZCgKm49AwW7rt0UgV4JV4/view">example 1</a>, <a href="https://drive.google.com/file/d/18GiXf3dBND5ZCgKm49AwW7rt0UgV4JV4/view">example 2</a>, or other light fields available online such as <a href="http://graphics.stanford.edu/data/LF/lfs.html">here</a>, we can explore the implications of different optical designs on downstream processing.

Warm up: Use the camera data to extract pinhole images from different viewpoints. Compare pinhole images to full-aperture images in terms of appearance, depth of field, and noise level. Explore spatial-angular slices (sometimes called “epipolar images”). Consider which sub-images would be best for stereo depth perception and depth from defocus, and test these hypotheses.

Project 1: Based on Liang, Chia-Kai, Yi-Chang Shih, and Homer H. Chen. "Light field analysis for modeling image formation." IEEE Transactions on Image Processing, model the light field sampling of an eye of your choice, in the style of fig 1 of Levin, Anat, William T. Freeman, and Frédo Durand. "Understanding camera trade-offs through a Bayesian analysis of light field projections." 

Project 2 Read Banks, Martin S., et al. "Why do animal eyes have pupils of different shapes?." Science Advances. Test the effect of pupil shape on stereo depth performance by simulating apertures from the light field data. Consider what makes a fair comparison and how the effects you observe might be exaggerated through optical design.

Project 3: Read Levin, Anat, et al. "Image and depth from a conventional camera with a coded aperture." ACM transactions on graphics (TOG). Simulate their aperture code and depth recovery algorithm, and compare to non-coded depth from defocus.

## Jennifer Groh

1. How does a brain create/read out a multiplexed code?  Figure 7 of Caruso et al 2018 provides a back-of-the-envelope sketch of a circuit model of some possibilities for the de-multiplexing.  Try implementing one of these, or come up with your own!

## Taraz Lee

## Mariam Aly

1. Design and program a behavioral experiment that assesses relational attention and/or perception. The task should be designed to tax hippocampal representations, based on the knowledge you acquired from the assigned readings above. You can use PsychoPy, PsychToolBox for Matlab, Gorilla, jsPsych, Pavlovia, or similar software. 

For inspiration, read about the behavioral tasks in these studies:
• <a href="../_static/pdfs/aly/cordova-turkbrowne-aly-2019-hippocampus.pdf">Córdova N.I., Turk‐Browne N.B., & Aly M. (2019). Focusing on what matters: Modulation of the human hippocampus by relational attention. _Hippocampus,29_(11):1025-37. DOI: 10.1002/hipo.23082.</a>

• <a href="../_static/pdfs/aly/ruiz-meager-agarwal-aly-2020-jocn.pdf">Ruiz N.A., Meager M.R., Agarwal S., Aly M. The medial temporal lobe is critical for spatial relational perception. _Journal of Cognitive Neuroscience, 32_(9):1780-95. DOI:10.1162/jocn_a_01583.</a>

## Kohitij Kar

For background, I added two tutorials:
1. A [Jupyter notebook](https://github.com/CSHL-comp-neuro-vision/tutorials/blob/main/python/NoiseCorrection/noise_correction_demo_py.ipynb) with a tutorial demonstrating the effects of misrepresenting relationships between variables due to noise in their estimates and how to retrieve the true relationship using noise correction techniques.  
2. [A tutorial on predicting neural activity using deep net features.](https://github.com/kohitij-kar/prediction_demo)

Project idea:  
Core Concept: Develop a strategy to determine which models of vision are most aligned with a Target model, using ResNet-50 as a proxy for primate object recognition. Usually that target model is a human or monkey -- but for our project let’s use a fully accessible ANN like ResNet-50. The goal is to optimize experimental design to discriminate between competing models that claim to be good representations of the Target.  

Key Components:  
1. Target Model: ResNet-50 (standing in for primate visual system). 
2. Competing Models: Various vision models claiming to represent the Target (you can use AlexNet, other ResNets, ViT, simCLR etc).  
3. Experimental Design Optimization: Techniques to generate stimuli that best differentiate between models. (Look up [Golan et al. 2020](https://www.pnas.org/doi/10.1073/pnas.1912334117)).  
4. Evaluation Metrics: Methods to quantify alignment between competing models and the Target (look up: [Rajalingham et al. 2018](https://www.jneurosci.org/content/38/33/7255)).

Methodology:  
1. Implement ResNet-50 as the Target model.  
2. Select or implement a set of competing vision models. 
3. Develop an optimization framework for experimental design:  
	a. Use techniques like controversial stimuli generation ([Golan et al. 2020](https://www.pnas.org/doi/10.1073/pnas.1912334117)).  
	b. Aim to maximize differences in responses amongst competing models.  
4. Generate optimal stimuli sets to achieve 3b  
5. Evaluate model responses to these stimuli   
6. Analyze the results to rank competing models based on their alignment with the Target  
7. Ground truth retrieval and validation (see below)  

The main idea for the validation is -- develop identical models: when the Target and reference models are identical, the experimental design should:  
• Generate stimuli that produce nearly identical responses across both models.  
• Result in a discrimination task that fails to find significant differences.  
• Show high correlation and low divergence measures between identical model outputs (compared to other models).  

One can generate identical models by:  
• Implementing multiple runs of the same model with different initializations.  
• Linearly transform the feature space of a model to another space and treat them as separate models.  
• This project leverages existing model to optimize experimental design that helps develop a more targeted evaluation of those same vision models.  


## Lindsey Glickfeld

In [Barbera et al.](https://www.sciencedirect.com/science/article/pii/S0896627321007856), we used a simple subunit based, Hubel and Wiesel style model to predict V1 responses to gratings and plaids, and then to test the effect of mask phase on these responses. 

1.  This model built V1 cells that only have one (excitatory) subunit and orientation preference/selectivity is defined by the elongation of the long axis of the RF. However, V1 neurons typically have an "on" and an "off" subunit, and in the mouse orientation preference/selectivity is defined by the axis of overlap of these subunits. Build a new version of this model with on/off subunits and test whether this changes (A) the magnitude of cross orientation interactions and (B) the sensitivity of those interactions to mask phase.

2.  In cat/primate V1, plaid stimuli drive responses that are component selective.  However, in mouse V1, responses can be either pattern and component selective. Use this simple subunit model to (A) determine whether V1 neurons are component and/or pattern selective and (B) test whether these responses are sensitive to mask phase. 

The code for the model in Barbera et al. can be found <a href="https://figshare.com/collections/BarberaPriebeGlickfeld_Neuron_2022/5677225/">here</a>, see _Figure4_model_code.m_.
