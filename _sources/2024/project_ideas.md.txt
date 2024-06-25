# Project Ideas

## EJ Chichilnisky

1. Download Pillow data set. Fit GLM. Test if we can do better with some kind of subunit model fit (Shah 2020 paper)?

## John Serences

## Eero Simoncelli

1. Metamers: given a model and a reference image, stochastically generate a new image whose model representation is identical to that of the reference image.  [ref:  Freeman & Simoncelli 2011]

2. Eigendistortions: given a model and a reference image, compute the image perturbation that produces the smallest and largest changes (in terms of Euclidean distance) in the model response space.  [ref: Berardino et al 2017]

3. Maximal differentiation (MAD) competition: given two models that measure distance between images and a reference image, generate pairs of images that optimally distinguish the models. Specifically, synthesize a pair of images that the first model says are equi-distant from the reference while the second model says they are maximally/minimally distant from the reference. Synthesize a second pair with the roles of the two models reversed.  [ref: Wang & Simoncelli 2008]

4. Geodesics: given a model and two images, attempt to synthesize a sequence of images that lie on the shortest ("geodesic") path in the model's representation space. [ref. Henaff & Simoncelli 2016]

(note from Dan: not really a project idea, but a tool you could use in a project)
My lab has produced a python library of tools to explore vision models by  synthesizing novel informative images.
This includes Metamers (as per my talk yesterday), Eigendistortions (Berardino 2017), Maximal differentiation (MAD) competition (Wang 2008), and Geodesics (Henaff 2016). Might be useful for some students in the course.  If you want to link it from Slack or from the course GitHub, it’s [here]https://github.com/LabForComputationalVision/plenoptic/: Kate Bonnen is an expert user and someone to ask questions about it.

## Stephanie Palmer

## Jonathan Pillow

1. Temporal vs. rate coding in retina (or any other dataset you'd like to examine).
How much information is carried in the precise timing of spikes vs. in slowly-fluctuating spike rates?  One way to address this question is to decode spikes under models that incorporate vs. ignore precise spike timing information. 
Project idea;  compare decoding under an LNP model and a Poisson GLM with spike history filters. How much (if any) additional information can you recover about the stimulus when you incorporate spike history?

Relevant refs: 

 - Pillow et al. “Spatio-temporal correlations and visual signalling in a complete neuronal population”.  Nature (2008).

See also: [GLM tutorial code](https://github.com/pillowlab/GLMspiketraintutorial).

2. Can a Poisson GLM exhibit divisive normalization?
Divisive normalization is one of the putative "canonical computations" carried out in the brain, but we still lack a good computational understanding of how it's carried out, or how to infer statistical models that can exhibit divisive normalization.
 
The Poisson generalized linear model (GLM) for spike trains provides a simple, tractable statistical model of spike trains. But can it exhibit divisive normalization?
 
Relevant refs: 

• <a href="../_static/pdfs/pillow/carandini-heeger-2011-natrevneuro.pdf">Carandini & Heeger (2011) Normalization as a canonical neural computation. _Nat Rev Neurosci, 13_:51-62. DOI:10.1038/nrn3136.</a>
<a href="../_static/pdfs/pillow/carandini-heeger-1994-science.pdf">Carandini & Heeger. (1994). Summation and division by neurons in primate visual cortex. _Science, 264_(5183):1333-1336. DOI:10.1126/science.8191289.</a>
• <a href="../_static/pdfs/pillow/Pillow_etal_2008.pdf">Pillow et al. (2008). Spatio-temporal correlations and visual signalling in a complete neuronal population. _Nature, 454_(21). DOI:10.1038/nature07140.</a>

 3. Compare GLM and deep neural networks - try out deep learning on some real neural data. See e.g.:
• [Deep convolutional models improve predictions of macaque V1 responses to natural images](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006897).

• [Multilayer Recurrent Network Models of Primate Retinal Ganglion Cell Responses](https://openreview.net/forum?id=HkEI22jeg).

• A recent paper argued that “modern machine learning” outperforms GLMs in many cases (although in the detailed results shown, GLM outperforms a deep neural network on most of the examples considered). Download their datasets and see if you can do better:
• [Paper](https://www.frontiersin.org/articles/10.3389/fncom.2018.00056/full)
• [Data](https://github.com/KordingLab/spykesML/tree/master/data)
(There are a lot of possible ways to think about improving: the paper did not consider different nonlinearities and made only limited attempts to select GLM features). 

## Jacob Yates

## Lea Duncker

## Ruth Rosenholtz

1. Combining predictions of peripheral vision with fixation data. We provide a subset of 100 images from the COCO-Periph dataset. The visualizations and code provided allow one to create visualizations of the information available for a (mostly) arbitrary fixation. We also provide eye tracking data for these images, from the COCO-Search 18 dataset from Greg Zelinsky. Observers executed these fixations while performing a search task. This combination of model predictions and eye tracking data should enable a number of interesting projects. For instance, consider the sequence of fixation locations, {(fx_i, fy_i), (fx_i+1, fy_i+1)}. Was the object at (fx_i+1, fy_i+1) likely identifiable when fixating (fx_i, fy_i), according to the peripheral vision model? In which case what might be the purpose of that saccade?

2. Many aspects of peripheral vision get worse in a roughly linear way. Acuity worsens as an approximately linear function of eccentricity, as does the critical spacing of crowding, as do hyperacuity and other aspects of vision. Van Essen and Anderson (1995) and others have suggested that this makes the information encoded about a stimulus relatively invariant to viewing distance. Under what circumstances does this hold, and when does it fail? Does it matter that the different linear functions have different slopes and intercepts?

## Rachel Denison

1. Maximally informative time points. We don’t need to pay attention at every moment, because sometimes nothing interesting is happening. Given a movie clip and a task that you specify, build a system that will learn the time points (frames in the movie) that are most informative for completing the task. You can use movies and tasks with varying degrees of complexity, so consider starting as simply as possible and building up from there!

2. Timing a brain process. Many aspects of neural control—including the control of visual attention—involve generating precisely timed brain activity. Build a neural network that delivers an output spike at a specified temporal interval following an input stimulus. Consider trying different timing mechanisms used by the brain, including ramping, oscillations, and trajectories through a state-space. How does the temporal precision of your output spike depend on the length of the interval? If you have solved the problem for one fixed interval, can you build a network that can generate an arbitrary temporal interval? Can you build a network that can learn a new temporal interval?

3. Contending with temporal uncertainty. Sometimes we know approximately when an important event will occur, but we don’t have perfect timing information. Such temporal uncertainty can arise from internal sources, like imprecision in our timing estimates, or external sources, like stochasticity in event times (e.g., a bus that comes approximately every 15 minutes but can be a little early or late). Consider a task in which a single stimulus appears with temporal uncertainty on each trial and the observer has to make some report on it. Given some source of temporal uncertainty that you specify, how should the observer allocate attention over time to maximize task performance across trials? You will need to make some assumptions about 1) how attention can be allocated across time (if there are no constraints, the observer could just attend all the time) and 2) how the amount of attention at the time of the stimulus relates to task performance.

4. On a different note, if you are interested in visual metacognition, the Confidence Database is a great resource of behavioral data with ~150 datasets and counting. There are many possible analysis projects that could be done using <a href="https://osf.io/s46pr/">these data</a> by  <a href="../_static/pdfs/denison/rahnev-et-al-2020-nhb.pdf">Rahnev et al. (2020). The Confidence Database. _Nature Human Behaviour, 4_(3):317-325.</a>

## Tony Movshon

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

a. The average correlation between each pair of neurons (this could be noise or signal correlation, depending on the data set you generated).\

b. The dimensionality of the shared variability (e.g. by calculating the proportion variance explained by the first k principal components for k=1:n)\

c. For the overachievers among you, calculate some fancy measurements too, such as communication subspace dimensionality if you modeled multiple brain areas (good code <a href="https://github.com/joao-semedo/communication-subspace">here</a>) or average or modal controllability (good code at #3 <a href="https://complexsystemsupenn.com/codedata">here</a>; start with the correlation matrix with the diagonal set to 0 instead of 1). If you would like to experiment with topological data analysis, I can provide code for that too.\

d. Next, make some change to your model that will affect the shared variability (maybe add in a common noise source, or change some model parameters) and repeat the calculations in #a-c. Can you gain some insight into how those numbers are related?\

e. Possible publishable extension: Do these calculations in a real data set (yours? Or several from my lab are available if you would like). Which ways of quantifying shared variability are most closely associated with behavior, stimuli, task condition, or some other quantity you think is important?

## Madineh Sedigh-Sarvestani

## Ione Fine

## Emma Alexander

## Jennifer Groh

1. How does a brain create/read out a multiplexed code?  Figure 7 of Caruso et al 2018 provides a back-of-the-envelope sketch of a circuit model of some possibilities for the de-multiplexing.  Try implementing one of these, or come up with your own!

## Taraz Lee

## Mariam Aly

1. Design and program a behavioral experiment that assesses relational attention and/or perception. The task should be designed to tax hippocampal representations, based on the knowledge you acquired from the assigned readings above. You can use PsychoPy, PsychToolBox for Matlab, Gorilla, jsPsych, Pavlovia, or similar software. \

For inspiration, read about the behavioral tasks in these studies:\
• <a href="../_static/pdfs/aly/cordova-turkbrowne-aly-2019-hippocampus.pdf">Córdova N.I., Turk‐Browne N.B., & Aly M. (2019). Focusing on what matters: Modulation of the human hippocampus by relational attention. _Hippocampus,29_(11):1025-37. DOI: 10.1002/hipo.23082.</a>\
• <a href="../_static/pdfs/aly/ruiz-meager-agarwal-aly-2020-jocn.pdf">Ruiz N.A., Meager M.R., Agarwal S., Aly M. The medial temporal lobe is critical for spatial relational perception. _Journal of Cognitive Neuroscience, 32_(9):1780-95. DOI:10.1162/jocn_a_01583.</a>\

## Kohitij Kar

## Lindsey Glickfeld

In [Barbera et al.](https://www.sciencedirect.com/science/article/pii/S0896627321007856), we used a simple subunit based, Hubel and Wiesel style model to predict V1 responses to gratings and plaids, and then to test the effect of mask phase on these responses. 

1.  This model built V1 cells that only have one (excitatory) subunit and orientation preference/selectivity is defined by the elongation of the long axis of the RF. However, V1 neurons typically have an "on" and an "off" subunit, and in the mouse orientation preference/selectivity is defined by the axis of overlap of these subunits. Build a new version of this model with on/off subunits and test whether this changes (A) the magnitude of cross orientation interactions and (B) the sensitivity of those interactions to mask phase.

2.  In cat/primate V1, plaid stimuli drive responses that are component selective.  However, in mouse V1, responses can be either pattern and component selective. Use this simple subunit model to (A) determine whether V1 neurons are component and/or pattern selective and (B) test whether these responses are sensitive to mask phase. 

The code for the model in Barbera et al. can be found <a href="https://figshare.com/collections/BarberaPriebeGlickfeld_Neuron_2022/5677225/">here</a>, see _Figure4_model_code.m_.

