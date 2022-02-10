# Range Images

## What are Range Images (距離影像)

### 1. 3D Point Cloud

Typically, the sensor data provided by a lidar scanner is represented as a `3d point cloud`, where each point corresponds to the measurement of a single lidar beam. Each point is described by a coordinate in `(x, y, z)` and additional attributes such as `the intensity of the reflected laser pulse `or even a `secondary return caused by partial reflection at object boundaries`.

```
3D point cloud 中儲存每個點的三維座標(x,y,z)
及其他額外屬性，如: 反射的強度，二次回波等等的。
```

In the following figure, a point cloud is shown where the brightness of a 3d point encodes the intensity of the laser reflection.

![](images/3d-point-cloud-and-camera.png)

As can be seen, the rear sections of the preceding vehicles and the wall on the right side are clearly visible with high intensity values in the birds-eye-view on the left, whereas the road surface or even the side of the vehicle in the center lane do hardly register at all.

### 2. Range Images (Depth Images)

An alternative form of representing lidar scans are `range images`. `This data structure holds 3d points as a 360 degree "photo"` of the scanning environment with the `row dimension` denoting the `elevation angle` of the laser beam and the `column dimension` denoting the `azimuth(方位角)`. With each incremental rotation around the z-axis, the lidar sensor returns a number of range and intensity measurements, which are then stored in the corresponding cells of the range image.

```
將從採集器到場景中個點的距離值作為像素值的圖像
它直接反應了景物可見表面的幾何形狀。
```

In the figure below, a point $\vec p$ in space is mapped into a range image cell, which is indicated by the corresponding `azimuth angle` $\alpha_p$ and the `inclination(傾角)` $b_p$ of the sensor. In the literature, $\alpha_p$ is often referred to as `yaw` whereas $b_p$ is called `pitch`.

```
Range Image: Row and Column

- Row: 仰角 (belta, pitch)
- Column: 方位角 (alpha, yaw)
```

In this example, only the range (i.e. the target distance) of $\vec p$ is stored in the cell. *However, in the Waymo dataset, the range image structure stores `range`, `intensity`, `elongation` and the `vehicle pose` at the time the measurement was created*.

![](images/3d-points-into-range-images.png)

#### Elongation (點雲延伸率)

The `elongation` of the laser pulse beyond its nominal width in conjunction with the intensity can be useful for classifying atmospherical conditions such as rain, fog or dust. Experiments conducted by Waymo suggest that a signal with high elongation and low intensity suggests the presence of atmospherical hazards.

LiDAR超出其標稱寬度的延伸與Intensity(強度)一起可用於對大氣條件進行類，如:`高延伸率但是低強度(低反射)的點一般為灰塵、霧、雨`。Waymo 進行的實驗表明，具有高伸長率和低強度的信號表明存在大氣危害。

Now that you have a first understanding of the concept of range images, let us visualize them properly.

## Visualizing Range Images

Please see [l1_examples - load_range_image](https://github.com/kaka-lin/nd013-c2-fusion-exercises/blob/main/lesson-1-lidar-sensor/examples/l1_examples.py)

In the example, output is `(64, 2650, 4)`, we now know that a `range image has 64 lines and 2650 columns`. From the previous section, we know that the top lidar covers a horizontal angle of 360°. This means that each column in the range image covers an arc of $\frac{360°}{2650}$ = 0.1358°,  which corresponds to a horizontal resolution of ≈8' angular minutes.

In order to compute the vertical resolution, we need to make use of the minimum and maximum inclination (i.e. pitch).
