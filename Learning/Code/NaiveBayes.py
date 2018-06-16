import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

#Read in the data into a pandas dataframe
dataFile = 'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv'
features = ['label', 'message']
texts = pd.read_table(dataFile, header=None, names=features)

#If you want to see it's size
#texts.shape

#If you want to see its top 5 or 10 or whatever
#texts.head()

#If you want to see the unique labels
#texts.label.unique()

#Lets convert the discrete "lable" into a numerical value we can work with
#Some examples will show you doing this as a .map and then doing it manually but this 
#Should work in the general sense
sms['labelNum'] = sms.label.astype('category')


#Let's use a classic example with the iris set
iris = load_iris()
X = iris.data
y = iris.target


