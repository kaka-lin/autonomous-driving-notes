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


def gaussian(x, mean, std):
    std2 = np.power(std, 2)
    return (1 / np.sqrt(2* np.pi * std2)) * np.exp(-.5 * (x - mean)**2 / std2)


# Parameter Update
def gaussian_update(gauss1: Gaussian, gauss2: Gaussian) -> Gaussian:
    mean1 = gauss1.mean
    std1 = gauss1.std
    mean2 = gauss2.mean
    std2 = gauss2.std

    new_mean = (np.power(std1, 2) * mean2 + np.power(std2, 2) * mean1) / (std1**2 + std2**2)
    new_std = np.sqrt(1 / ((1 / std1**2) + (1 / std2**2)))

    new_gauss = Gaussian(new_mean, new_std)
    return new_gauss

# Motion Update
def motion_update(gauss1: Gaussian, gauss2: Gaussian) -> Gaussian:
    mean1 = gauss1.mean
    variance1 = gauss1.variance
    mean2 = gauss2.mean
    variance2 = gauss2.variance

    new_mean = mean1 + mean2
    new_variance = variance1 + variance2

    new_gauss = Gaussian(new_mean, variance=new_variance)
    return new_gauss


if __name__ == "__main__":
    print(gaussian(10, 8, 2)) # 0.12098536225957168
    print(gaussian(10, 10, 2)) # 0.19947114020071635

    # Gaussion Update
    #   Gaussian(mean, std, variance)
    print(">>> Gaussian Update <<<")

    gauss1 = Gaussian(10, 2)
    gauss2 = Gaussian(12, 2)
    new_gauss = gaussian_update(gauss1, gauss2)
    print("New mean: {}, new std: {}, new variance: {}".format(
        new_gauss.mean, new_gauss.std, new_gauss.variance))

    gauss1 = Gaussian(10, np.sqrt(8))
    gauss2 = Gaussian(13, np.sqrt(2))
    new_gauss = gaussian_update(gauss1, gauss2)
    print("New mean: {}, new std: {}, new variance: {}".format(
        new_gauss.mean, new_gauss.std, new_gauss.variance))

    # Motion Update
    print(">>> Motion Update <<<")

    gauss1 = Gaussian(8, variance=4)
    gauss2 = Gaussian(10, variance=6)
    new_gauss = motion_update(gauss1, gauss2)
    print("New mean: {}, new std: {}, new variance: {}".format(
        new_gauss.mean, new_gauss.std, new_gauss.variance))

    gauss1 = Gaussian(10, variance=4)
    gauss2 = Gaussian(12, variance=4)
    new_gauss = motion_update(gauss1, gauss2)
    print("New mean: {}, new std: {}, new variance: {}".format(
        new_gauss.mean, new_gauss.std, new_gauss.variance))
