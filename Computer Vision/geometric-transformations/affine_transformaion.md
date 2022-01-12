# Affine transformation

```
A geometric transformation that preserves lines and parallelism
```

Affine transformation是一種保留點,直線和平面的線性映射方法,
通常用在*校正幾何失真(geometric distortions)或是變形(deformations)上*。

## Formula

General affine transformation (homogeneous coordinates):

$f(x_2,y_2) = Af(x_1,y_1) + B$

![](img/affine_transformaion.png)

線性轉換(Linear Transformation)定義: $f(a+b) = f(a)+f(b)$

![](img/affine_transformaion_2.png)

## Type of affine transformation

Affine Transformation 是一種混合的線性二維幾何轉換，而混合的線性轉換包括：`位移`、`放大縮小`、`旋轉` 以及 `Shearing` 的操作。

### Resizing (Scale)

![](img/affine_scale_2.png)
![](img/affine_scale.png)

```
cx specifies the scale factor along the x axis
cy specifies the scale factor along the y axis
```

### Translation

![](img/affine_translation_2.png)
![](img/affine_translation.png)

```
tx specifies the displacement along the x axis
ty specifies the displacement along the y axis
```

### Shear

![](img/affine_shear_2.png)
![](img/affine_shear.png)

```
sx specifies the the shear factor along the x axis
sy specifies the the shear factor along the y axis
```

### Rotation

![](img/affine_rotation_2.png)
![](img/affine_rotation.png)

```
q specifies the angle of rotation
```

## Reference

1. [Self Driving Car Engineer Nanodegree](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013)

2. [Affine transformation - MATLAB & Simulink](https://www.mathworks.com/discovery/affine-transformation.html)

3. [Affine transformation @ 拾人牙慧](https://silverwind1982.pixnet.net/blog/post/160691705)
