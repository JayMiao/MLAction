# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range('20130101', periods=6)
# print dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# print df

df2 = pd.DataFrame({  'A' : 1.,
                      'B' : pd.Timestamp('20130102'),
                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                      'D' : np.array([3] * 4,dtype='int32'),
                      'E' : pd.Categorical(["test","train","test","train"]),
                      'F' : 'foo' })
# print df2
# print df.sort_index(axis=1, ascending=False)
# print df
# print df.sort_values(by='B', ascending=False)

# print df2.loc[0:2,['E']]
# print df.iloc[[1,2,4],[0,2]]
# print df.loc[[1,2,4],[0,2]]

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102',periods=6))
# print s1

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1

print df1.drop('E', axis=1)
print df1.dropna(how='any')
print df1.fillna(value=5)
print df.mean(0)
print df.mean(1)