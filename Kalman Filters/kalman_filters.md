# Kalman Filters (卡爾曼濾波器)

`卡爾曼濾波器`又稱為`最佳線性濾波器(輸出值為輸入值的線性組合)`，為實現簡單、純時間域的濾波器。卡爾曼濾波器能夠從時間序列中不完全、包含雜訊的測量中，估計出系統的狀態，但系統必須是線性與動態的。在實現過程中，所有關於不確定性的關係(雜訊)，都會用到共變異數 (covariate) 矩陣。

複習: [Gaussian distribution](https://github.com/kaka-lin/autonomous-driving-notes/tree/master/Kalman%20Filters/Gaussian)

  - [Kalman Filters 原理](#kalman-filters-原理)
  - [Kalman Filters](#kalman-filters)
  - [Kalman Filters 公式](#kalman-filters-公式)

實作: [kalman_concept](kalman_concept.py), [kalman_basic](kalman_basic.py), [kalman.py](kalman.py), or [EKF/predict_update.py](https://github.com/kaka-lin/nd013-c2-fusion-exercises/blob/main/lesson-3-EKF/exercises/starter/1_predict_update.py)

## Kalman Filters 原理

卡爾曼濾波器的主要步驟有兩個: `Measurement Update` and `Prediction`。讓我們先從簡單的一維公式開始，來理解原理。

![](images/kalman.png)

### Measurement Update or Correction (量測更新):

- Requires a [product](https://classroom.udacity.com/courses/cs373/lessons/48739381/concepts/487235990923#)
- Uses [Bayes rule](https://classroom.udacity.com/courses/cs373/lessons/48739381/concepts/487221690923#)

將`當前感測器量測的資訊`與`上一時刻得到的預測資訊`融合。將兩個常態分佈`相乘`，得到`當前系統狀態的最佳估測值`。如下所示:

![](images/measurement_update_1.png)
![](images/measurement_update_3.png)

公式:

![](images/measuremen_update_formula.png)

### Motion Update or Prediction (預估)

- Involves a `convolution` or simply an `addition`
- Uses [total probability](https://classroom.udacity.com/courses/cs373/lessons/48739381/concepts/486736290923#)


根據`上一時刻最佳估測值`和`系統方程`預測當前時刻的系統狀態。會得到一個`預測值`，如下所示:

![](images/prediction_1.png)

公式:

![](images/prediction_formula.png)


### How kalman filters work

![](images/kalman_work_2.png)

從上圖可觀察:

- t = 2, 綠色高斯分佈:它只有位置的資訊但沒有速度相關的資訊。

    但如果將在 prediction step 算出的值 (prior) 與 measurement step 算出的值相乘，會得到一個當前系統狀態的最佳估測值，他是一個高斯分佈 (上圖中紅綠相交的黑色高斯分佈)。這個高斯分佈對位置與速度都有一個很好的估測 (分別投影至 x 及 v)。

    且如果採用這個高斯分佈進行下一個 Prediction step，會發現前進至下一個黑色的高斯分佈，此正式 t = 3 做一樣事情的結果。

這就是卡爾曼濾波器的工作原理。

## Kalman Filters

有了上述基本觀念後，我們來看以下範例:

![](images/kf-example.png)

That is the main idea of the Kalman filter

![](images/kf-overview.png)


1. Start with an initial guess of state
2. Then we predict the state to the next time stamp.

    - The Gaussian gets wider and flatters through the model `uncertainty`

3. Then we measure our actual state including some noise
4. And we correct our prediction using the measurements
5. Then we predict again to the next timestamp and so on

### Kalman Filtes Noise

![](images/kf-noise-1.png)

因為更新資訊都是根據 `prediction` and `measurement`。那我們在多大程度上相信這兩個輸入是正確的，我們更相信哪一個？

Actually, this decision depends on our sensors and our application. We have two different sets of parameters that are relevant for this weighting

![](images/kf-noise-2.png)

1. Covariance of process noise Q
   - small Q: the motion will vary only little, so we trust our motion model to be quite accurate  and the prediction will get a higher weight
2. Covariance of measuremant noise R
   - small R: we trust our measurement to contain only little noise and the measurement update will be higher weighted than the prediction

![](images/kf-noise-3.png)

- F,f: `state transition function`.

    - f: non-linear function
    - F: linear matrix function

- Covariance Q tells us how much the noise varies

    The bigger in entries Q, the more acceleration and braking we expect

    ```
    Q should be quite high: emergency braking assist
    ```

- H: `heuristic measurement function`

    The bigger in entries R, the measurements are quite noisy and may differ a lot from actual state.

### 1D Example

![](images/kf-noise-4.png)

## Kalman Filters 公式

![](images/kf-equations.png)

卡爾曼濾波器有五個公式，分兩個部份:

### 1. Prediction

```
X(k) = F(k) * X(k-1) + B(k) * U(k)
P(k) = F(k) * P(k-l) * F^T(k) + Q(k)
```
- X: estimate
- P: estimate covariance matrix
- F: state-transition model
- B: control-input model
- U: control vector (motion vector)
- Q: the covariance of the process noise

![](images/kalman_formula_prediction.png)

![](images/kalman_formula_prediction_2.png)

### 2. Measurement Update

```
Y(k) = Z(k) - H(k) * X(k)
S(k) = H(k) * P(k) H^T(k) + R(k)
K(k) = P(k)* H^T(k) * S^-1(k)
```

- Z: measurement vector
- H: measurement function
- R: the covariance of the measurement noise
- Y:  is the `residual` with `covariance S`
- K:  is the `Kalman gain` which weights prediction in comparison to measurement.

![](images/kalman_formula_measurement.png)

![](images/kalman_formula_measurement_2.png)

## Reference

- [Kalman filter, Wiki](https://en.wikipedia.org/wiki/Kalman_filter)
- [一維空間的卡爾曼濾波器 Kalman Filter (FORTH語言)](https://ohiyooo2.pixnet.net/blog/post/405342657)
- [卡爾曼濾波 (Kalman Filter), 拾人牙慧](https://silverwind1982.pixnet.net/blog/post/167680859)
- [理解卡爾曼濾波器](https://www.itread01.com/content/1541553003.html)
