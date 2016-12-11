# -*- coding: utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.datasets import make_regression

import autograd.numpy as np
from autograd import grad

import numpy.linalg as linalg

EPS = 1e-15
def binary_crossentropy(actual, predicted):
    predicted = np.clip(predicted, EPS, 1 - EPS)
    return np.mean(-np.sum(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted)))

class LogisticRegression():
    def __init__(self, lr = 0.001, C = 0.01, tolerance=0.00001, max_iters = 1000):
        self.lr = lr
        self.C = C
        self.tolerance = tolerance
        self.max_iters = max_iters
        self.errors = []
        self.theta = []
        self.n_samples, self.n_features = None, None

    def fit(self, X, y=None):
        self.X = X; self.y = y
        self.n_samples = np.shape(X)[0]
        self.n_features = np.shape(X)[1]

        # 初始化theta
        self.theta = np.random.normal(size=(self.n_features + 1), scale=0.5)
        # 添加截距
        b = np.ones([self.n_samples, 1])
        self.X = np.concatenate([b, X], axis=1)

        # 进行模型训练: 随机梯度下降
        self._gradient_descent()

    def _gradient_descent(self):
        theta = self.theta
        errors = [self._cost(self.X, self.y, theta)]
        for i in range(1, self.max_iters + 1):
            # 创建实例
            cost_d = grad(self._loss)
            delta = cost_d(theta)
            theta -= self.lr * delta

            errors.append(self._cost(self.X, self.y, theta))
            error_diff = np.linalg.norm(errors[i-1] - errors[i])
            print error_diff
            if error_diff < self.tolerance:
                print "iteration: %d , torance: %d" % (i , self.tolerance)
                break

    @staticmethod
    def sigmoid(x):
        return 1.0 / (1 + np.exp(-x))

    def _loss(self, theta):
        loss = binary_crossentropy(self.y, self.sigmoid(np.dot(self.X, theta)))
        #add penalty
        penalty = self._add_penalty(loss, theta)
        return loss + penalty

    def _cost(self, X, y, theta):
        prediction = X.dot(theta)
        error = binary_crossentropy(y, prediction)
        return error

    def _add_penalty(self, loss, w):
        loss += (0.5 * self.C) * (w[:-1] ** 2).mean()
        return loss


def classification():
    # Generate a random binary classification problem.
    X, y = make_classification(n_samples=1000, n_features=100, n_informative=75, random_state=1111, n_classes=2,
                               class_sep=2.5, )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1111)

    model = LogisticRegression(lr=0.01, max_iters=500, C=0.01)
    model.fit(X_train, y_train)
    # predictions = model.predict(X_test)
    # print('classification accuracy', accuracy(y_test, predictions))


if __name__ == '__main__':
    classification()