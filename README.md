# Deep Mask Detect

A deep learning convolutional neural network (CNN) developed in Python using various libraries including [PyTorch](https://pytorch.org/), [pandas](https://pandas.pydata.org/), and [Matplotlib](https://matplotlib.org/) and trained on over 2000 images to identify and classify face images into 5 classes, namely:

1. Cloth mask (cloth)
2. N95 mask (n95)
3. N95 mask with valve (n95v)
4. No face mask (nfm)
5. Surgical mask (srg)

## Data

For training, validation, and assessment a combination of over 2000 images were taken from a [Kaggle dataset](http://kaggle.com/datasets/omkargurav/face-mask-dataset) and [GDeltaProj dataset](https://blog.gdeltproject.org/a-set-of-massive-new-datasets-for-cataloging-mask-appearances-on-television-news/).
Figure below illustrates the percentage distribution of classes.

<p alt="ER diagram-image" align="center"><a href="https://github.com/rmanaem/deep-mask-detect/blob/master/appendix/phase2/biased/download.png"><img src="https://github.com/rmanaem/deep-mask-detect/blob/master/appendix/phase2/biased/download.png?raw=true"/></a></p>
To balance the dataset, roughly 2000 images were randomly selected and used.

## Preprocessing

Preprocessing of images was done in three steps:

- Image resizing
- Image channel conversion to RGB
- Normalization

Images are first transformed into dimensions of 300 x 300. Then, the mean value of each RGB channel is calculated across the entire training data and subtracte3d from both the training and testing sets to normalize the image across each channel in the range [-1,1]. Each channel is then divided by its standard deviation that is computed over the training set. Images are then processed in batch sizes of 16. Generally, this practice helps reduce skewness in the dataset which in turn helps the model learn accurately.

## CNN Architecture

The specifications of the CNN model are as follows:

- Input image: 300 x 300 x 3

- Convolutional block 1: The input image is fed into the first convolution layer that uses a filter of size 5 along with a stride factor of 2 - followed by a Rectifier Linear Unit (ReLU) activation function.

- 2D-max pooling layer 1: The pooling layer uses a kernel of size 2 and stride 2 and produces a feature map of size 256 x 256 x 128

- Convolutional block 2: The second convolution layer is fed a kernel of size 3 along with a stride factor of 2.

- Convolutional block 3: The third convolution layer is again fed a kernel of size 3 along with a stride factor of 2.

- Convolutional block 4: The fourth convolution layer is again fed a kernel of size 3 along with a stride factor of 2.

- Max pooling layer 2: The pooling layer uses a kernel of size 2 and stride 1 and produces a feature map of size 32 x 32 x 64

- Convolutional block 5: The final block is fed a kernel of size 4 along with a stride factor of 2 producing a feature map of size 5 x 5 x 64.

Each convolutional block is composed of a 2-dimensional
convolution and a 2-dimensional batch normalization to accelerate deep neural networks with momentum 0.1. In addition, a 2-dimensional dropout regularization with probability of 0.1 was applied after calling the ReLU activation function.

### Hypre-parameters

- Loss function: cross-entropy, it summarizes the average difference between the actual and predicted probability distributions.

- Batch size: 16

- Epochs: 20

- Optimizer: Adam

- Learning rate: 0.00146

- Weight decay: 1e-6

- Dropout: 0.1
