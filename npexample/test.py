# -*- coding: utf-8 -*-

import numpy as np
from sklearn import preprocessing
a = [ 1., 2.,  0.]
b = [1,-1,2]
print np.var(a)
print np.mean(a)
print (a - np.mean(a)) / np.sqrt(np.var(a))
# print preprocessing.scale(a)
# print preprocessing.scale(b)