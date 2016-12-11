# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
# plt.style.use('ggplot')

df = pd.read_csv('winequality-red.csv' , sep = ';')
X = df.drop('quality' , 1).values
X = scale(X)
y1 = df['quality'].values

pd.DataFrame.hist(df, figsize = [15,15])
plt.show()
# y = y1 <= 5
# plt.figure(figsize=(20,5))
#
# plt.subplot(1, 2, 1)
# plt.ylabel('count')
# plt.xlabel('original target value')
# plt.hist(y1)
#
# plt.subplot(1, 2, 2)
# plt.xlabel('aggregated target value')
# plt.hist(y)
#
# # plt.show()
#
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# from sklearn import neighbors, linear_model
# knn = neighbors.KNeighborsClassifier(n_neighbors=5)
# knn_model_1 = knn.fit(X_train, y_train)
# # print knn_model_1.score(X_test,y_test)
#
# from sklearn.metrics import classification_report
# y_true, y_pred = y_test, knn_model_1.predict(X_test)
# print classification_report(y_true, y_pred)

