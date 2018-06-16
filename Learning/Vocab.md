# Words You Need To Know
This will be in my own words, and updated upon request if something I write is
insufficent or incorrect. I'm not doing any lookups on this stuff so it's
possible!
* Feature:
    A Feature is literally any piece of relevant information that we have on a
    data point. This can be discrete (an integer or floating point value) or
    categorical (Red vs. Blue / True vs. False). We usually choose to encode all
    categorical values if we care about them. 
* Sparse Matrix: 
    This term most often comes up when you are discussing textual data sets.
    When looking at this type of data your best bet is to represent the data as
    a bag of words, which means each word gets a column, and the data point in
    that column is how often it is used in that data point (sentence, paper,
    whatever). This means that you are going to have a lot of 0's in every
    single row. This is a tremendous waste of space in general if you are using
    native arrays or tables, so pandas/numpy/scipy/sklearn store it as a special data
    type called a Sparse Matrix which is usually written in Fortran and much
    more performant, speed and storage wise. You can read more [here](https://machinelearningmastery.com/sparse-matrices-for-machine-learning/)

* Recall: 
    //TODO

* Accuracy: 
    //TODO

* Precision:
    //TODO

* ROC: 
    More formally known as the "Receiver Operating Characteristic Curve", the
    ROC curve is a plot whose goal is to illustrate the diagnostic ability of a
    classifier as its threshold is varied. You create it by plotting the True
    Positive Rate (recall) agains the False Positive Rate (fall-out, Type I
    error)

* AUC: 
    The abbreviated version of "Area Under Curve" is a metric used for
    classifiers when the label you are aiming for is binary (0,1). It's a good
    metric after accuracy or f1 scores but is less natural. It's measured in the
    real range [0,1] just like the above mentioned, however its calculation is
    much different. In this case the area under the curve refers the the area
    underneath a ROC curve (explained above). AUC is especially useful if your
    classifier is particularly label heavy towards one of the two choices. A
    mediocre ML algorithm can score high accuracy by learning to just choose
    true a bunch of times, but if that is the case it will score a 0.5 in AUC.
    [Resource](http://fastml.com/what-you-wanted-to-know-about-auc/) 
