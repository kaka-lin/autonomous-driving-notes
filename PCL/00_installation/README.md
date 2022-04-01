# Install Point Cloud Library

- [C++ version](#point-cloud-library)
- [Python version](#python-pcl)

---

## Docker environment

### Build

```bash
$ docker build --rm \
    -t kakalin/pcl:1.8.0 \
    -f pcl.Dockerfile  .
```

### Python Only

```bash
$ docker build --rm \
    -t kakalin/python-pcl:1.8.0 \
    -f python-pcl.Dockerfile .
```

#### Runming

```bash
$ xhost +local:root
```

```bash
$ docker run --rm -it \
    --gpus all \
    -e DISPLAY=$DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    --volume="$PWD:/root/PCL" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --privileged \
    kakalin/pcl:1.8.0 # or kakalin/python-pcl:1.8.0
```

## [Point Cloud Library](https://github.com/PointCloudLibrary/pcl)

### Install on the platform

- [Linux](https://pcl-tutorials.readthedocs.io/en/latest/compiling_pcl_posix.html)

## [python-pcl](https://github.com/strawlab/python-pcl)

### Requirements

- Python 2.7.6, 3.5.x
- pcl 1.8.1 (apt install)
- Cython <= 0.25.2

### Install (Ubuntu 18.04)

#### 1. Install pcl

    ```bash
    $ sudo apt-get update -y
    $ sudo apt-get install libpcl-dev -y
    ```
#### 2. Install requirement modules

    ```bash
    $ pip3 install --upgrade pip
    $ pip3 install cython
    $ pip3 install numpy
    ```

#### 3. Install `python-pcl`

    ```bash
    $ wget https://github.com/strawlab/python-pcl/archive/v0.3.0rc1.tar.gz
    $ tar zxvf v0.3.0rc1.tar.gz
    $ cd python-pcl-0.3.0rc1

    $ python3 setup.py build_ext -i
    $ python3 setup.py install
    ```

### Troubleshooting

#### 1. `ImportError: No module named pcl_visualization`

Reference: [ubuntu下成功安裝python-pcl及各種錯誤解決](https://www.twblogs.net/a/5c378893bd9eee35b3a59e63)

- Modify the setup.py that can find your vtk

    ```
    # VTK use?
    ext_args['include_dirs'].append('/usr/include/vtk-6.3')
    ```

- Uncomment

    ```
    Extension("pcl.pcl_visualization", [
                            "pcl/pcl_visualization.pyx"], language="c++", **ext_args),
    ```
