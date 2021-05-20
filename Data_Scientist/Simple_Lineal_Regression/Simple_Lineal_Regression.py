#Regreción lineal simple
import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('../machinelearning-az/datasets/Part 2 - Regression/Section 4 - Simple Linear Regression/Salary_Data.csv')
#print(dataset)

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values
#print(y)

entrenamiento = X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=1/3, random_state=0)
print(entrenamiento)