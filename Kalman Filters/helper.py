from math import *

import numpy as np


class Gaussian:
    """Summary of class here.

    Attributes:
        mean: μ (平均值)
        std: standard deviation, σ (標準差)
        variance: σ^2 (變異數)
    """
    def __init__(self, mean=0, std=None, variance=None) -> None:
        self._mean = mean

        if std:
            self._std = std
            self._variance = self._std ** 2
        elif variance:
            self._variance = variance
            self._std = np.sqrt(self._variance)
        else:
            print('Initial error, missing parameters "std" or "variance", please at least select one.')
            raise AttributeError

    @property
    def mean(self):
        return self._mean

    @mean.setter
    def mean(self, val):
        self._mean = val

    @property
    def std(self):
        return self._std

    @std.setter
    def std(self, val):
        self._std = val
        self._variance = self._std ** 2

    @property
    def variance(self):
        return self._variance

    @variance.setter
    def variance(self, val):
        self._variance = val
        self._std = np.sqrt(self._variance)


# Measurement Update (Correction)
def measurement_update(gauss1: Gaussian, gauss2: Gaussian) -> Gaussian:
    mean1 = gauss1.mean
    std1 = gauss1.std
    mean2 = gauss2.mean
    std2 = gauss2.std

    new_mean = (np.power(std1, 2) * mean2 + np.power(std2, 2) * mean1) / (std1**2 + std2**2)
    new_std = np.sqrt(1 / ((1 / std1**2) + (1 / std2**2)))

    new_gauss = Gaussian(new_mean, new_std)
    return new_gauss


# Prediction (Motion Update)
def prediction(gauss1: Gaussian, gauss2: Gaussian) -> Gaussian:
    mean1 = gauss1.mean
    variance1 = gauss1.variance
    mean2 = gauss2.mean
    variance2 = gauss2.variance

    new_mean = mean1 + mean2
    new_variance = variance1 + variance2

    new_gauss = Gaussian(new_mean, variance=new_variance)
    return new_gauss


# This cell helps implement a matrix class for you.
# Make sure to run this first before you continue!
class matrix:
    # implements basic operations of a matrix class
    def __init__(self, value):
        self.value = value
        self.dimx = len(value)
        self.dimy = len(value[0])
        if value == [[]]:
            self.dimx = 0

    def zero(self, dimx, dimy):
        # check if valid dimensions
        if dimx < 1 or dimy < 1:
            raise ValueError("Invalid size of matrix")
        else:
            self.dimx = dimx
            self.dimy = dimy
            self.value = [[0 for row in range(dimy)] for col in range(dimx)]

    def identity(self, dim):
        # check if valid dimension
        if dim < 1:
            raise ValueError("Invalid size of matrix")
        else:
            self.dimx = dim
            self.dimy = dim
            self.value = [[0 for row in range(dim)] for col in range(dim)]
            for i in range(dim):
                self.value[i][i] = 1

    def show(self):
        for i in range(self.dimx):
            print(self.value[i])
        print(' ')

    def __add__(self, other):
        # check if correct dimensions
        if self.dimx != other.dimx or self.dimy != other.dimy:
            raise ValueError("Matrices must be of equal dimensions to add")
        else:
            # add if correct dimensions
            res = matrix([[]])
            res.zero(self.dimx, self.dimy)
            for i in range(self.dimx):
                for j in range(self.dimy):
                    res.value[i][j] = self.value[i][j] + other.value[i][j]
            return res

    def __sub__(self, other):
        # check if correct dimensions
        if self.dimx != other.dimx or self.dimy != other.dimy:
            raise ValueError("Matrices must be of equal dimensions to subtract")
        else:
            # subtract if correct dimensions
            res = matrix([[]])
            res.zero(self.dimx, self.dimy)
            for i in range(self.dimx):
                for j in range(self.dimy):
                    res.value[i][j] = self.value[i][j] - other.value[i][j]
            return res

    def __mul__(self, other):
        # check if correct dimensions
        if self.dimy != other.dimx:
            raise ValueError("Matrices must be m*n and n*p to multiply")
        else:
            # multiply if correct dimensions
            res = matrix([[]])
            res.zero(self.dimx, other.dimy)
            for i in range(self.dimx):
                for j in range(other.dimy):
                    for k in range(self.dimy):
                        res.value[i][j] += self.value[i][k] * other.value[k][j]
            return res

    def transpose(self):
        # compute transpose
        res = matrix([[]])
        res.zero(self.dimy, self.dimx)
        for i in range(self.dimx):
            for j in range(self.dimy):
                res.value[j][i] = self.value[i][j]
        return res

    # Thanks to Ernesto P. Adorio for use of Cholesky and CholeskyInverse functions
    def Cholesky(self, ztol=1.0e-5):
        # Computes the upper triangular Cholesky factorization of
        # a positive definite matrix.
        res = matrix([[]])
        res.zero(self.dimx, self.dimx)

        for i in range(self.dimx):
            S = sum([(res.value[k][i])**2 for k in range(i)])
            d = self.value[i][i] - S
            if abs(d) < ztol:
                res.value[i][i] = 0.0
            else:
                if d < 0.0:
                    raise ValueError("Matrix not positive-definite")
                res.value[i][i] = sqrt(d)
            for j in range(i+1, self.dimx):
                S = sum([res.value[k][i] * res.value[k][j] for k in range(self.dimx)])
                if abs(S) < ztol:
                    S = 0.0
                try:
                    res.value[i][j] = (self.value[i][j] - S)/res.value[i][i]
                except:
                    raise ValueError("Zero diagonal")
        return res

    def CholeskyInverse(self):
        # Computes inverse of matrix given its Cholesky upper Triangular
        # decomposition of matrix.
        res = matrix([[]])
        res.zero(self.dimx, self.dimx)

        # Backward step for inverse.
        for j in reversed(range(self.dimx)):
            tjj = self.value[j][j]
            S = sum([self.value[j][k]*res.value[j][k] for k in range(j+1, self.dimx)])
            res.value[j][j] = 1.0/tjj**2 - S/tjj
            for i in reversed(range(j)):
                res.value[j][i] = res.value[i][j] = -sum([self.value[i][k]*res.value[k][j] for k in range(i+1, self.dimx)])/self.value[i][i]
        return res

    def inverse(self):
        aux = self.Cholesky()
        res = aux.CholeskyInverse()
        return res

    def __repr__(self):
        return repr(self.value)
