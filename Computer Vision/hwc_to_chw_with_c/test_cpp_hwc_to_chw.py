import cv2
import numpy as np

import cv_example


if __name__ == "__main__":
    chw_img_list = cv_example.hwc2chw()

    height = 576
    width = 768
    channels = 3

    chw_img = np.array(chw_img_list, dtype=np.uint8).reshape((channels, height, width))
    print("CHW Image Shape: ", chw_img.shape)
    hwc_img = np.transpose(chw_img, (1, 2, 0))
    print("HWC Image Shape: ", hwc_img.shape)
    cv2.imshow("HWC Image from CHW Image", hwc_img)
    cv2.waitKey(0)
