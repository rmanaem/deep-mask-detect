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
