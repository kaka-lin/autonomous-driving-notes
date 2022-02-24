import numpy as np

from helper import *


def kalman(measurements, measurements_var,
           motion, motion_var,
           mean, variance):

    gauss = Gaussian(mean, variance=variance)
    for n in range(len(measurements)):
        # Measurement update
        gauss = measurement_update(gauss, Gaussian(measurements[n], variance=measurements_var))
        print("[measurement_update] mean: {}, variance: {}".format(
            gauss.mean, gauss.variance))

        # Prediction (Motion update)
        gauss = prediction(gauss, Gaussian(motion[n], variance=motion_var))
        print("[prediction]         mean: {}, variance: {}".format(
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
