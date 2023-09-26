#!/usr/bin/python
# coding: utf-8

import numpy as np


def getBinBorders(data, BINS):
    '''
        Calculate bin borders for a given dataset and a given number of bins

        Args:
            data: given dataset for which the borders should be calculated
            BINS: number of bins to create

        Returns:
            Returns a bin sequence as well as a boolean value stating whether
            the sequence is on log scale. For example:

            [0.0, 0.5, 1.0], False
    '''

    BIN_MIN = np.nanmin(data)
    BIN_MAX = np.nanmax(data)

    # use logspace for bin ranges over 100 or values below 0
    if (BIN_MAX - BIN_MIN) > 100 and (BIN_MAX * BIN_MIN) > 0:
        BIN_MIN = np.log10(BIN_MIN)
        BIN_MAX = np.log10(BIN_MAX)

        return np.logspace(BIN_MIN, BIN_MAX, BINS+1), True
    # check weather the dataset is constant
    elif (BIN_MAX - BIN_MIN) == 0 or np.isnan(BIN_MAX - BIN_MIN):
        return None, False
    # linear case
    else:
        return np.linspace(BIN_MIN, BIN_MAX, BINS+1), False


def getXvalues(bin_borders):
    '''
        Returns bin centers and halfwidhts for given bin sequence
    '''

    left, right = bin_borders[:-1], bin_borders[1:]
    points = {'center': left + right,
              'halfwidth': right - left}
    points.update((key, value * 0.5) for key, value in points.items())

    return points['center'], points['halfwidth']


def getYvalues(values, nfiles, BINS, bin_borders, lifetime=None, weights=None):
    '''
        Returns y values for weighted histograms, as well as its errors
        Errors are sq roots of summed up weights divided by nfiles
    '''

    # get mapping between values and bins
    binIndex = np.digitize(values, bin_borders)
    # no weights given: assume poisson distribution -> errors = stdev
    if weights is None:
        y, _ = np.histogram(values, bins=bin_borders)
        errors = np.sqrt(y)
    # for given weights, the error is calculated as the sq root of the sum of squared weights
    # due to icecube's simulations, weights need to be normed tu number of given files
    # and multiplied by the lifetime to obtain event numbers (without nfiles & lifetime -> Hz)
    else:
        y = np.zeros(BINS)
        errors = np.zeros(BINS)
        for i, v in enumerate(binIndex):
            if v > 0 and v <= BINS and i < len(weights):
                # bin numbering starts with 1, while arrays don't
                # therefore reduce the bin number by 1
                # sum up all weights of each bin v and divide it by nof
                y[v-1] += (weights[i] / nfiles)
                errors[v-1] += (weights[i] / nfiles) ** 2

        errors = np.sqrt(errors)
        if lifetime:
            y *= lifetime
            errors *= lifetime

    return y, errors

