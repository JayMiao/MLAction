# -*- coding: utf-8 -*-
import numpy as np
import os.path
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score

__mode_path__ = 'data/model.pkl'
data = np.loadtxt('data/train.csv', delimiter=',', dtype=np.str, skiprows=1)
y, X = data[:, 0], data[:, 1:]
clf = RandomForestClassifier(n_estimators=100, criterion='entropy', max_features=500, n_jobs=-1, verbose=1)
clf
print cross_val_score(clf, X, y, cv=5, n_jobs=-1, verbose=1)

# if os.path.isfile(__mode_path__):
#     clf = joblib.load(__mode_path__)
# else:
#     data = np.loadtxt('data/train.csv', delimiter=',', dtype=np.str, skiprows=1)
#     y, X = data[:,0], data[:,1:]
#
#     clf = RandomForestClassifier(n_estimators=100, criterion='entropy', max_features=500)
#     clf.fit(X, y)
#     joblib.dump(clf, __mode_path__)






