# -*- coding: utf-8 -*-

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)
# clf = svm.LinearSVC(penalty='l1', loss='squared_hinge', dual=False)
# scores = cross_val_score(clf, iris.data, iris.target, cv=5)
# print scores
# exit()

# print clf.score(X_test, y_test)
# clf = svm.SVC(kernel='linear', C=0.5).fit(X_train, y_train)
# print clf.score(X_test, y_test)
# clf = svm.SVC(kernel='sigmoid', C=0.5).fit(X_train, y_train)
# print clf.score(X_test, y_test)
# clf = svm.SVC(kernel='rbf', C=0.5).fit(X_train, y_train)
# print clf.score(X_test, y_test)
# clf = svm.SVC(kernel='poly', degree=3, C=0.5).fit(X_train, y_train)
# print clf.score(X_test, y_test)

scaler = preprocessing.StandardScaler().fit(X_train)
X_train_transformed = scaler.transform(X_train)
clf = svm.SVC(C=1).fit(X_train_transformed, y_train)
X_test_transformed = scaler.transform(X_test)
scores = clf.score(X_test_transformed, y_test)
print scores