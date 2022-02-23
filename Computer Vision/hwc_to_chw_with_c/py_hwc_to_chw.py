import cv2
import numpy as np


if __name__ == "__main__":
    img = cv2.imread("images/dog.jpg") # (HWC)
    print("Original Shape: ", img.shape)
    height, width, channels = img.shape
    size = height * width * channels
    img_flat = img.flatten()

    chw_img_list = [None] * size
    for c in range(channels):
        for h in range(height):
            for w in range(width):
                src_idx = h * width * channels + w * channels + c
                dst_idx = c * height * width + h * width + w
                chw_img_list[dst_idx] = img_flat[src_idx]

    print(chw_img_list[24], chw_img_list[567])
    chw_img = np.array(chw_img_list).reshape((channels, height, width))
    print("CHW Image Shape: ", chw_img.shape)
    hwc_img = np.transpose(chw_img, (1, 2, 0))
    print("HWC Image Shape: ", hwc_img.shape)
    cv2.imshow("HWC Image from CHW Image", hwc_img)
    cv2.waitKey(0)
