# How to use Iterative Closest Point algorithm in PCL

Iterative Closest Point algorithm can determine if one Point Cloud is just a rigid transformation of another by minimizing the distances between the points of two Point Clouds and rigidly transforming them.

## Running in Container

Download the docker image that we provided

```sh
$ docker pull kakalin/pcl:1.8.0
```

Running

```sh
$ ./run.sh
```

### Compiling and Running

Compile:

```sh
$ ./build.sh
```

Run:

```bash
$ ./iterative_closest_point
```

You will see something similar to:

```sh
Saved 5 data points to input:
(0.352222,-0.151883,-0.106395)
(-0.397406,-0.473106,0.292602)
(-0.731898,0.667105,0.441304)
(-0.734766,0.854581,-0.0361733)
(-0.4607,-0.277468,-0.916762)
size:5
Transformed 5 data points:
(1.05222,-0.151883,-0.106395)
(0.302594,-0.473106,0.292602)
(-0.0318983,0.667105,0.441304)
(-0.0347655,0.854581,-0.0361733)
(0.2393,-0.277468,-0.916762)
has converged:1 score: 1.1956e-13
           1 -2.30968e-07 -2.98023e-08          0.7
 -2.1793e-07            1 -7.82311e-08  -1.2368e-07
 7.45058e-08  4.09782e-08            1   3.8743e-08
           0            0            0            1
```

## Reference

- [How to use iterative closest point](https://pointclouds.org/documentation/tutorials/iterative_closest_point.html)
