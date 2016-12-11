# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

iris = load_iris()
clf = AdaBoostClassifier(n_estimators=1000)
scores = cross_val_score(clf, iris.data, iris.target)

print scores.mean()