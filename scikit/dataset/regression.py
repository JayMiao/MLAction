# -*- coding: utf-8 -*-

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

def getRegressionData():
    X, y = make_regression(n_samples=10000, n_features=100, n_informative=75, n_targets=1,
                           noise=0.05, random_state=1111, bias=0.5)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1111)
    return X_train, X_test, y_train, y_test