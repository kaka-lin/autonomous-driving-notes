import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mean, std):
    std2 = np.power(std, 2)
    return (1 / np.sqrt(2* np.pi * std2)) * np.exp(-.5 * (x - mean)**2 / std2)


if __name__ == "__main__":
    gauss_1 = gaussian(10, 8, 2) # 0.12098536225957168
    gauss_2 = gaussian(10, 10, 2) # 0.19947114020071635

    print("Gauss(10, 8, 2): {}".format(gauss_1))
    print("Gauss(10, 10, 2): {}".format(gauss_2))

    # 標準高斯分佈
    mean = 0
    variance = 1
    std = np.sqrt(variance)

    # Plot between -10 and 10 with .001 steps.
    x = np.arange(-5, 5, 0.001)
    gauss = []
    for i in x:
        gauss.append(gaussian(i, mean, std))
    gauss = np.array(gauss)

    plt.plot(x, gauss)
    plt.show()
