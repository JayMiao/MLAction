# -*- coding: utf-8 -*-
from sklearn import svm
import numpy as np

X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
print np.bincount(Y)
exit()
model = svm.SVC


print model.predict([[2,2]])
print model.support_vectors_
print model.support_
print model.n_support_
