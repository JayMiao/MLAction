# coding: utf-8
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

## user
# 读取user -> feature选择 -> 缺失值填充 -> 对性别编码 -> 归一化
users = pd.read_csv('data/users.csv', sep=',')
user_features = ["RESPID","GENDER","AGE","Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10","Q11","Q12","Q13","Q14","Q15","Q16","Q17","Q18","Q19"]
users = users[user_features]

# fill nan
users['AGE'].fillna(39.2, inplace=True) # 这里精度要控制下否则后面变成整数会溢出
users['Q16'].fillna(0, inplace=True)
users['Q18'].fillna(0, inplace=True)
users['Q19'].fillna(0, inplace=True)

# 对性别进行编码
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse=False)
users_vec = vec.fit_transform(users.to_dict(orient='record')).astype(int)
users = pd.DataFrame(users_vec, columns=vec.feature_names_)

# 不同单位 归一化
from sklearn.preprocessing import scale
respid = users['RESPID']
users = users.drop('RESPID', 1)
users_scaled = pd.DataFrame(scale(users), columns=users.columns)
users_scaled = pd.concat([respid,users_scaled], axis=1)


# 读取train数据
train = pd.read_csv('data/train.csv', sep=',')

# 获得artist的平均分
artist_mean_rating = train[['Artist','Rating']].groupby('Artist').mean()

# words获取 缺失值填充
words = pd.read_csv('data/words.csv', sep=',')
words = words.drop(['HEARD_OF','OWN_ARTIST_MUSIC'],1)
words.fillna(0, inplace=True)

"""
回归模型
对每一位artist建立一个model
feature 用户对 artist 的评价 来自words users train
target  用户对 artist 的评分
"""
from sklearn.metrics import mean_squared_error
import math
def rmse(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    return math.sqrt(mse)

from sklearn.linear_model import Lasso
from sklearn import neighbors
from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
artists = train['Artist'].unique()
artist_model = {}
for artist in artists:
    train_features = train[train.Artist == artist]
    train_features = train_features[['User', 'Rating']]

    words_features = words[words.Artist == artist]
    words_features = words_features.drop('Artist', 1)

    X = pd.merge(train_features, words_features, left_on='User', right_on='User')
    X = pd.merge(X, users_scaled, left_on='User', right_on='RESPID')
    y = X['Rating']
    X = X.drop(['User','Rating'], 1)
    # print X.columns
    # exit()

    # clf = Lasso(alpha=0.5)
    clf = XGBRegressor(n_estimators=100, learning_rate=0.05)
    # clf = RandomForestRegressor(n_estimators=100, max_features='sqrt')
    # clf = svm.SVC()

    #RMSE check
    # print np.sqrt(mean_squared_error(y, clf.predict(X)))

    # k-fold check
    # score = cross_val_score(clf, X, y, cv=5, n_jobs=-1, scoring='neg_mean_squared_error')
    # print np.sqrt(abs(score.mean()))
    # artist_model[artist] = clf

'''
Predict:
'''
test = pd.read_csv('data/test.csv', sep=',')
users_test = test[['User','Artist','Time']]
features_list = X.columns
test = pd.merge(test, users_scaled, left_on='User', right_on='RESPID')
test = pd.merge(test, words_features, left_on='User', right_on='User')
result = []
count = 100;
for user_test in users_test.values:
    user = user_test[0]
    artist = user_test[1]
    print "Predicting: User - %s", user
    model = artist_model[artist]

    row = test[(test.User == user) & (test.Artist == artist)]
    if row.empty:
        score = artist_mean_rating['Rating'][artist]
    else:
        row = row[features_list]
        score = model.predict(row)
    result.append(score)

print result;














