#Import libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matolotlib inline

dataset_train = pd.read_csv("Google_Stock_Price_Train.csv")
dataset_train.head()

training_set = dataset_train.iloc[:,1:2].values
print (training_set)
print (training_set.shape)
