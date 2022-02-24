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
