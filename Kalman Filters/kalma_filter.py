from Gaussian.gaussian import *


# Parameter Update
# def gaussian_update(gauss1: Gaussian, gauss2: Gaussian) -> Gaussian:
#     mean1 = gauss1.mean
#     std1 = gauss1.std
#     mean2 = gauss2.mean
#     std2 = gauss2.std

#     new_mean = (np.power(std1, 2) * mean2 + np.power(std2, 2) * mean1) / (std1**2 + std2**2)
#     new_std = np.sqrt(1 / ((1 / std1**2) + (1 / std2**2)))

#     new_gauss = Gaussian(new_mean, new_std)
#     return new_gauss


# Motion Update
# def motion_update(gauss1: Gaussian, gauss2: Gaussian) -> Gaussian:
#     mean1 = gauss1.mean
#     variance1 = gauss1.variance
#     mean2 = gauss2.mean
#     variance2 = gauss2.variance

#     new_mean = mean1 + mean2
#     new_variance = variance1 + variance2

#     new_gauss = Gaussian(new_mean, variance=new_variance)
#     return new_gauss


def kalman(measurements, measurements_var,
           motion, motion_var,
           mean, variance):

    gauss = Gaussian(mean, variance=variance)
    for n in range(len(measurements)):
        # Measurement update
        gauss = gaussian_update(gauss, Gaussian(measurements[n], variance=measurements_var))
        print("[measurement update] mean: {}, variance: {}".format(
            gauss.mean, gauss.variance))

        # Motion update
        gauss = motion_update(gauss, Gaussian(motion[n], variance=motion_var))
        print("[motion update]      mean: {}, variance: {}".format(
            gauss.mean, gauss.variance))


if __name__ == "__main__":
    measurements = [5., 6., 7., 9., 10.]
    measurements_var = 4.
    motion = [1., 1., 2., 1., 1.]
    motion_var = 2.
    mean = 0.
    variance = 10000.

    kalman(measurements, measurements_var,
           motion, motion_var,
           mean, variance)
