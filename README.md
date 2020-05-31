# Diagnosis of MSI gastrointestinal tumors

### Project goal

Gastrointestinal tumors can display microsatellite instability (MSI). It is known patients with MSI gastrointestinal tumors benefit from immunotherapy treatment, while patients with no-MSI tumors do not respond to the same extent.
The goal of this project is to classify biopsy images of gastrointestinal tumors into tumors with MSI and MSS (microsatellite stability) to train a Machine Learning model and/or a neural network that, in the end, can predict whether a new biopsy image belongs to an MSI or MSS class.
To achieve this goal, the following were pursued:
- Decrease the dimensionality of images through different image prepocessing techniques: one or three channels, resize, noise filters, thresholds, FFT, PCA
- Train several Machine Learning algorithms for classification optimizing their parameters and different neural network topologies: choose the best model based on metrics (e.g. accuracy)
- Develop an API to predict new images received from HTML requests

### Material and methods

A [dataset](https://www.kaggle.com/joangibert/tcga_coad_msi_mss_jpg) containing 192.312 biopsy images of MSI and MSS gastrointestinal tumors was used to perform this project via programming in Python language. 
Image preprocessing was carried out using OpenCV and Skimage libraries, as well as Numpy and Pandas to manage data from images.
Scikit-Learn, H2O and Keras libraries were used to train models and neural networks and make the predictions on new images.

#### - Image preprocessing

As mentioned above, different preprocessing methods were performed to reduce the dimensionality of images. However, all these techniques not only decrease image dimensions, but also cause the images to lose information. Reducing dimensionality at the cost of losing information may not be a good idea in images where the differences are subtle. In fact, good metrics were not obtained with the tested models and neural network when images were preprocessed. 
Therefore, original images were used to perform the trainings.

#### - Model trainings

Different classifier models from Scikit-Learn library were tested: K-Nearest Neighbors, Decision Trees, Support Vector Machines, with Decision Trees class obtaining the best metrics. Moreover, three neural network topologies with different number of layers were used. 
Finally, the neural network with best metrics was used to train the whole dataset. To perform the complete training, an instance in Google Cloud Platform was used.

#### -API development


