# -*- coding: utf-8 -*-
import logging

from autograd import grad
import autograd.numpy as np

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Change to DEBUG to see convergence
logging.basicConfig(level=logging.ERROR)
np.random.seed(1000)
EPS = 1e-15

def unhot(function):
    """Convert one-hot representation into one column."""
    def wrapper(actual, predicted):
        if len(actual.shape) > 1 and actual.shape[1] > 1:
            actual = actual.argmax(axis=1)
        if len(predicted.shape) > 1 and predicted.shape[1] > 1:
            predicted = predicted.argmax(axis=1)
        return function(actual, predicted)

    return wrapper

@unhot
def classification_error(actual, predicted):
    return (actual != predicted).sum() / float(actual.shape[0])


@unhot
def accuracy(actual, predicted):
    return 1.0 - classification_error(actual, predicted)

def binary_crossentropy(actual, predicted):
    predicted = np.clip(predicted, EPS, 1 - EPS)
    return np.mean(-np.sum(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted)))

class LogisticRegression():
    def __init__(self, lr=0.001, C=0.01, tolerance=0.0001, max_iters=1000):
        self.C = C
        self.tolerance = tolerance
        self.lr = lr
        self.max_iters = max_iters
        self.errors = []
        self.theta = []
        self.n_samples, self.n_features = None, None
        self.cost_func = binary_crossentropy

    def _loss(self, w):
        prediction = np.dot(self.X, w)
        prediction = self.sigmoid(prediction)
        loss = self.cost_func(self.y, prediction)
        loss += (0.5 * self.C) * np.linalg.norm(w[:-1])
        return loss

    def _cost(self, theta):
        prediction = np.dot(self.X, theta)
        error = self.cost_func(self.y, prediction)

        return error

    def fit(self, X, y=None):
        self.X = X
        self.y = y
        self.n_samples, self.n_features = X.shape

        # Initialize weights + bias term
        self.theta = np.ones(self.n_features + 1)

        # Add an intercept column
        self.X = self._add_intercept(self.X)

        self.theta, self.errors = self._gradient_descent()
        logging.info(' Theta: %s' % self.theta.flatten())

    @staticmethod
    def _add_intercept(X):
        b = np.ones([X.shape[0], 1])
        return np.concatenate([b, X], axis=1)

    @staticmethod
    def sigmoid(x):
        return 0.5 * (np.tanh(x) + 1)

    def predict(self, X=None):
        X = self._add_intercept(X)
        return self.sigmoid(X.dot(self.theta))

    def _gradient_descent(self):
        theta = self.theta
        errors = [self._cost(theta)]

        for i in range(1, self.max_iters + 1):
            # Get derivative of the loss function
            cost_d = grad(self._loss)
            # Calculate gradient and update theta
            delta = cost_d(theta)
            theta -= self.lr * delta

            errors.append(self._cost(theta))
            logging.info('Iteration %s, error %s' % (i, errors[i]))

            error_diff = np.linalg.norm(errors[i - 1] - errors[i])
            if error_diff < self.tolerance:
                logging.info('Convergence has reached.')
                break
        return theta, errors

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    X, y = make_classification(n_samples=1000, n_features=100, n_informative=75, random_state=1111, n_classes=2,
                               class_sep=2.5, )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1111)

    model = LogisticRegression(lr=0.01, max_iters=500, C=0.01)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print('classification accuracy', accuracy(y_test, predictions))