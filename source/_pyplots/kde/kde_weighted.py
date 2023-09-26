#!/usr/bin/env python
# vim:set ts=4 sts=4 sw=4 et:

import numpy as np
from sklearn.base import BaseEstimator
from sklearn.utils import check_random_state


def integrate_binned(x, y, binlims):
    x = x.flatten()
    y = y.flatten()
    n_int = len(binlims)-1
    pred_binned = np.zeros(n_int)
    for k in range(n_int):
        mask = (x > binlims[k]) & (x < binlims[k+1])
        pred_binned[k] = np.mean(y[mask])
    return pred_binned


def parzen_1d(X):
    X[np.greater(np.abs(X), 1.0)] = 0
    return X


def cosine_1d(X):
    X = parzen_1d(X)
    return np.cos(X * np.pi/2.0) * np.pi/4.0


def epanechnikov_1d(X):
    X = parzen_1d(X)
    return (3.0/4.0) * (1-np.square(X))


def linear_1d(X):
    X = parzen_1d(X)
    return (1.0 - np.abs(X))


def norm_1d(X):
    return np.exp(-0.5*np.square(X)) / np.sqrt(2.0*np.pi)


def tophat_1d(X):
    X = parzen_1d(X)
    return 0.5 * X


def tricube_1d(X):
    X = parzen_1d(X)
    return np.power(1-np.square(X), 3)*70.0/81.0


KERNEL_DICT = {
    'cosine': cosine_1d,
    'epanechnikov': epanechnikov_1d,
    'gaussian': norm_1d,
    'linear': linear_1d,
    'tophat': tophat_1d,
    'tricube': tricube_1d,
}


class KernelDensityWeighted(BaseEstimator):
    """Simple gaussian KDE, including weights.

    This class conforms to the scikit-learn API, so it can be used
    inside GridSearchCV.
    """

    def __init__(self, bandwidth=1.0, kernel='gaussian'):
        self.bandwidth = bandwidth
        self.kernel = kernel

    def fit(self, X, y=None, weights=None, bw_inc=None):
        self.support_ = np.ravel(X)[:, np.newaxis]
        if bw_inc is not None:
            if X.shape[0] != bw_inc.shape[0]:
                raise ValueError
            self.bw_local_ = np.sqrt(
                np.square(self.bandwidth) +
                np.square(bw_inc)
            )
        else:
            self.bw_local_ = None
        if weights is not None:
            if X.shape != weights.shape:
                raise ValueError
            self.weights_ = weights * (X.shape[0] / np.sum(weights))
        else:
            self.weights_ = None
        return self

    def predict(self, X):
        sup = self.support_
        n_sup = len(sup)
        if self.bw_local_ is not None:
            bw = self.bw_local_
        else:
            bw = self.bandwidth
        if self.weights_ is not None:
            wgt = self.weights_
        else:
            wgt = 1
        kernel_ = KERNEL_DICT[self.kernel]
        n_pred = X.shape[0]
        result = np.zeros((n_pred, ), dtype=np.float)
        for p in range(n_pred):
            kernel_dist = wgt * kernel_((X[p]-sup)/bw) / bw
            result[p] = np.sum(kernel_dist) / n_sup
        return result

    def predict_binned(self, binlims, n_sup=11):
        n_int = len(binlims-1)
        pred_binned = np.zeros(n_int)
        for k in range(n_int):
            X = np.linspace(binlims[k], binlims[k+1], n_sup)
            pred = self.predict(X)
            pred_binned[k] = np.mean(pred)
        return pred_binned

    def sample(self, n_samples=1, random_state=None):
        """Does not support local bandwidths of weights yet."""
        data = np.asarray(self.support_)
        rng = check_random_state(random_state)
        i = rng.randint(data.shape[0], size=n_samples)
        if self.kernel == 'gaussian':
            return np.atleast2d(rng.normal(data[i], self.bandwidth))

    def score(self, X):
        return np.sum(self.score_samples(X))

    def score_samples(self, X):
        N = self.support_.shape[0]
        log_density = np.log(self.predict(X))
        log_density -= np.log(N)
        return log_density
