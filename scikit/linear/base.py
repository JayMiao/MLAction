# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data
print np.shape(diabetes.data)

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20,:]
diabetes_X_test = diabetes_X[-20:,:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
print diabetes_y_test; exit()

# Create linear regression object
regr = linear_model.Lasso(alpha = 0.1)

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

print regr.coef_
error = ((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2).mean()
print error

score = regr.score(diabetes_X_test,diabetes_y_test)
print "Score: " , score

