# -*- coding: utf-8 -*-
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/train.csv', sep=',')
# X = df['label'].values
# print type(X)
#看下样例分布
# plt.hist(X, color='green')
# plt.show()

x = {'a': 1, 'b': 2}
xa = np.asarray(x)
print x['a']