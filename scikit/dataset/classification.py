# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

def getClasssificationData():
    X, y = make_classification(n_samples=1000, n_features=100, n_informative=75, random_state=1111, n_classes=2,
                           class_sep=2.5, )
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1111)