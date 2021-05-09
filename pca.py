import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt   

#load and tranpose csv data 
#Data fetched on 2021-05-08
csvDataT = pd.read_csv('ticks.norm.csv')
csvData = csvDataT.T

#Symbol column like AEFES,AKBNK,AKSA...
ticks = csvData.iloc[0]

#Data columns. First column contains name of features so removed
csvData = csvData.iloc[1:]

#Append Headers
csvData.columns = ticks

#Data contains Index number which is equals to feature columns count 
# (PE ratio, Earning per share... vs.)
csvData.index = [0] * csvData.shape[0]  
 
 
 #Actual PCA math and data reduction
centeredData = preprocessing.scale(csvData.T)
pca = PCA()   
pca.fit(centeredData)   
reducedData = pca.transform(centeredData)   
 
#Reformat data and prepare PCA result component labels for scatter graph
percentageVariance = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['Comp' + str(n) for n in range(1, len(percentageVariance)+1)]
  
#create pandas data frame matrix for 2d representation
frame = pd.DataFrame(reducedData, index=[*ticks], columns=labels)

#First 2 component of PCA analysis result contains most dominant data (out of 4 others in this case)
# Comp1 and Comp2 will be used to create scatter plot
plt.scatter(frame.Comp1, frame.Comp2)
plt.title('Bist 100 PCA Analysis (as 2021-05-08)')
plt.xlabel('Principle Component 1')
plt.ylabel('Principle Component 2')

for sample in frame.index:
    plt.annotate(sample, (frame.Comp1.loc[sample], frame.Comp2.loc[sample]))
plt.show()

 