# Kalman Filters (卡爾曼濾波器)

`卡爾曼濾波器`又稱為`最佳線性濾波器(輸出值為輸入值的線性組合)`，為實現簡單、純時間域的濾波器。卡爾曼濾波器能夠從時間序列中不完全、包含雜訊的測量中，估計出系統的狀態，但系統必須是線性與動態的。在實現過程中，所有關於不確定性的關係(雜訊)，都會用到共變異數 (covariate) 矩陣。

## Kalman Filters 原理

卡爾曼濾波器的主要步驟有兩個: `Measurement Update` and `Prediction`。讓我們先從簡單的一維公式開始，來理解原理。

![](images/kalman.png)

### Measurement Update or Correction (量測更新):

- Requires a [product](https://classroom.udacity.com/courses/cs373/lessons/48739381/concepts/487235990923#)
- Uses [Bayes rule](https://classroom.udacity.com/courses/cs373/lessons/48739381/concepts/487221690923#)

將`當前感測器量測的資訊`與`上一時刻得到的預測資訊`融合。將兩個常態分佈`相乘`，得到`當前系統狀態的最佳估測值`。如下所示:

![](images/measurement_update_1.png)
![](images/measurement_update_3.png)

#### 公式:

![](images/measuremen_update_formula.png)

### Motion Update or Prediction (預估)

- Involves a `convolution` or simply an `addition`
- Uses [total probability](https://classroom.udacity.com/courses/cs373/lessons/48739381/concepts/486736290923#)


根據`上一時刻最佳估測值`和`系統方程`預測當前時刻的系統狀態。會得到一個`預測值`，如下所示:

![](images/prediction_1.png)

#### 公式:

![](images/prediction_formula.png)

## Reference

- [Kalman filter, Wiki](https://en.wikipedia.org/wiki/Kalman_filter)
- [一維空間的卡爾曼濾波器 Kalman Filter (FORTH語言)](https://ohiyooo2.pixnet.net/blog/post/405342657)
- [卡爾曼濾波 (Kalman Filter), 拾人牙慧](https://silverwind1982.pixnet.net/blog/post/167680859)
- [理解卡爾曼濾波器](https://www.itread01.com/content/1541553003.html)
