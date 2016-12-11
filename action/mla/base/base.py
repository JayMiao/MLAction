# -*- coding: utf-8 -*-

import numpy as np

class BaseEstimator(object):
    X = None
    y = None
    y_required = True

    def _setup_input(self, X, y=None):
        if not isinstance(X, np.ndarray):
            X = np.ndarray(X)

        if X.size == 0:
            raise ValueError('Number of feature must be > 0')

        if X.ndim == 1:
            self.n_samples, self.n_feature = 1, X.shape
        else:
            self.n_samples, self.n_feature = X.shape[0], np.prod(X.shape[1:])

        self.X = X

        if self.y_required:
            if y is None:
                raise ValueError('Miss requed argument y')
            if not isinstance(y, np.ndarray):
                y = np.ndarray(y)
            if y.size == 0:
                raise ValueError('Number of feature must be > 0')
        self.y = y

    def fit(self, X, y=None):
        self._setup_input(X, y)
    def predict(self, X=None):
        if self.X is not None:
            return self._predict(X)
        else:
            raise ValueError('You must call `fit` before predict')

    def _predict(self):
        raise NotImplemented
