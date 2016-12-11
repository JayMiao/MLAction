# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# rng = pd.date_range('1/1/2012', periods=100, freq='S')
# ts = pd.Series(np.random.randint(0,500,len(rng)), index=rng)
# print ts
# print ts.resample('5Min')


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# print ts
# print '************************'
ts = ts.cumsum()
# print ts
ts.plot()
plt.show()
