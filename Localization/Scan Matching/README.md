# Scan Matching

Challenge: `Where is the robot with respect to the previous frame`

Give `a scan and a map`, or `a scan and a scan`, or `a map and a map`, and find the `rigid-body transformation (translation + rotation)` that aligns them best.


假設當前 frame 的 Lidar data 為 A，和它批配的另一個 frame data 為 B，
如果以 `A 為 起始點 (target/reference)`，`B 為下一個位置點 (source/measured)`，
我們的目的就是找出 `B -> A 的 rigid-body transformation 矩陣 (平移+旋轉)`，
如下範例:

在一台車上配有 LiDAR，它首先先掃描環境，然後汽車稍微移動並再次掃描環境

<p float="left">
  <img src="images/scan-matching_1.png" height="auto" width="600" />
  <img src="images/scan-matching_2.png" height="auto" width="600" />
</p>

如果我們將這兩個掃描並排顯示，會發現他們非常相似:

- 藍色掃描是汽車在時間 t 進行的第一次掃描
- 藍色掃描是汽車在時間 t+1 進行的第二次掃描

<p float="left">
  <img src="images/scan-matching_3.png" height="300" width="auto" />
  <img src="images/scan-matching_4.png" height="300" width="auto" />
</p>


所以:

- Scan matching compares two very similar lidar scans to get a transformation in the movement
- You then stitch together the transforms to localize
- The transforms can be represented mathematically by a transformation matrix, as below:

    ![](images/matrix-transformations.png)

## Transforms

A `pose` can be a `position`, which in 2D consists of a position $(x,y)$ and orientation $\theta$, in reference to the global coordinate system.

##### Example:

```
A pose vector is <1,2,π/6>

- a position: (1,2)
- an orientation: 30°.
```

A `pose offset` can also be a `representation of a delta in x,y,θ` in reference to the local coordinate system, `this is then a transformation that provides movement information`. This delta pose represents your transformation, how the object has moved with its $x,y,θ$ values in reference to its local coordinate frame.

##### For instance:

計算機器人從位置 <1,2,π/6> 開始，然後得到 <Δ1, Δ1, Δπ/6> 的位姿變換 (pose transform) 後的位置。

1. `Convert these vectors into transformation matrices`

    - vectors include pose vector and pose offset vector

    - *Transformation matrix*: $[[RT],[0,1]]$, where:
      - R: is the rotation (In 2D is 2x2, calculated from θ)
      - T: is the translation (In 2D is 2x1, contains the x and y offsets)

2. `Finding the new position and orientation`

    將由 pose vector 轉換程的 transformation matrix T1 與
    由 pose offset vector 轉換程的 transformation matrix T2 相承
    即可以得到包含新位置 (x,y) 和 新方向 (θ) 的變換矩陣。

    然後將該變換矩陣轉換為姿勢向量方便讀值。

## Iterative Closest Point (ICP)

由於採集設備不同、拍攝視角不同等等因素的影響，即使是同一個物體所得到的點雲也會有較大的差異，主要是旋轉或者平移的變化。對於一組圖像數據集中的兩幅圖像，需要通過尋找一種空間變換把一幅圖像映射到另一幅圖像，使得兩圖中對應於空間同一位置的點一一對應起來，從而達到信息融合的目的

```
找到一個 transformer matrix
使得 scan frames 之間最鄰近點的距離最小化
```

Step 1

<p float="left">
  <img src="images/icp-1.png" height="300" width="auto" />
  <img src="images/icp-2.png" height="300" width="auto" />
</p>


Step 2

<p float="left">
  <img src="images/icp-3.png" height="300" width="auto" />
  <img src="images/icp-4.png" height="300" width="auto" />
</p>

ICP has a `target(reference)` scan and a `source` scan.

- Associations are made between the source points and target points
- A transform that minimizes the sum of association's distances is performed

Steps 1 and 2 repeat until associations don't change, and ICP has converged or a certain number of iterations have been done.

### 優缺點

- 優點: 匹配效果最好的演算法，因為充分利用了每一個點
- 缺點: 速度慢，因為使用了所有的點雲

### Example of using ICP in PCL

Sample code: [ICP Example](https://github.com/kaka-lin/autonomous-driving-notes/tree/master/Localization/Scan%20Matching/icp_example)

Reference:
- [How to use iterative closest point](https://pointclouds.org/documentation/tutorials/iterative_closest_point.html)

### Scan Match Exercise

Using ICP to recover the path taken by robot traveling around a room that is only equipped with a single lidar sensor.

To complete this exercise, you'll be primarily filling in the ICP function.

- Part 1:

    - Create a PCL object that does ICP, give it the target in source points, and call align, that'll return and transform that best overlaps the source and target points.

    - Increase iterations.

        ```
        high enough iterations -> achieve convergence

        when the associations are no longer changing.
        ```
    - Transform Scan and Visualize it

- Part 2,3:
  - Save the transform that you have and use it for next time as the closets starting point.

如下圖所示:

<img src="images/scan-match-exercise.png" height="400" width="auto" />

#### Complete ICP Function

1. Convert Pose Vector to Transformation Matrix
2. Transform Source by starting pose (`pose offset`)

    ```
    new sorce = source *
                transformation_matrix (starting pose)
    ```
3. Creating PCL ICP object, set based on parametes.
    icp object's values: Transformed Source, Target, iterations

4. Then align to get transform
5. Multipy transform with starting pose

For the detail please see [here](https://github.com/kaka-lin/nd013-c3-localization-exercises/tree/master/Scan%20Matching/ICP).
