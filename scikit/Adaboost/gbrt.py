# -*- coding: utf-8 -*-

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

# X, y = make_hastie_10_2(random_state=0)
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=5, random_state=0)
# print cross_val_score(clf, X, y)


from sklearn.datasets import make_friedman1
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split


X, y = make_friedman1(n_samples=1200, random_state=0, noise=1.0)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1)
X_train, X_test = X[:200], X[200:]
y_train, y_test = y[:200], y[200:]
for i in range(10, 200, 10):
    clf = GradientBoostingRegressor(n_estimators=i, learning_rate=0.5, max_depth=2, random_state=0)
    clf.fit(X_train, y_train)
    print i ,  mean_squared_error(y_test, clf.predict(X_test))