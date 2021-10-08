# Quickstarts: Run CARLA with Docker

[CARLA in Docker](https://carla.readthedocs.io/en/latest/build_docker/)

Users can pull an image based on a CARLA release to run in a Docker container. This is useful for users who:


- Want to run CARLA without needing to install all dependencies
- Run multiple CARLA servers and perform GPU mapping
- Run the CARLA server without a display

## Running CARLA in a container (server)

### 1. Pull the CARLA image

You can pull either the latest CARLA image or a specific release version. In this example we using `0.9.11`.

```bash
$ docker pull carlasim/carla:0.9.11
```

### 2. Run the CARLA container

Different versions of CARLA support different graphics APIs which can affect the conditions in which the Docker image can run:

- `0.9.12: supports only Vulkan`
- `0.9.7 to 0.9.11: supports both Vulkan and OpenGL`

#### To CARLA 0.9.11 using OpenGL

```bash
$ docker run --rm \
    -e DISPLAY=$DISPLAY \
    --net=host \
    --gpus all \
    --runtime=nvidia \
    carlasim/carla:0.9.11 /bin/bash CarlaUE4.sh -opengl
```

##### Off-screen mode

Ref: [Carla 0.9.11 in a Docker fails to start](https://github.com/carla-simulator/carla/issues/3911#issuecomment-792287764)

```bash
$ docker run --rm \
    -e SDL_VIDEODRIVER='offscreen' \
    --net=host \
    --gpus all \
    --runtime=nvidia \
    carlasim/carla:0.9.11 /bin/bash CarlaUE4.sh -opengl
```

## Running client example

### 1. Install client library

Install corresponding version Python library.

#### 1-1. Get the corresponding version Python library

- Runing docker image

    ```bash
    $ docker run --rm -d \
        -e SDL_VIDEODRIVER='offscreen' \
        --net=host \
        --gpus all \
        --runtime=nvidia \
        carlasim/carla:0.9.11 /bin/bash CarlaUE4.sh -opengl
    ```
- Get container's ID

    ```bash
    $ docker ps -a
    ```

- Copy `.egg` file from container to local

    ```bash
    $ docker cp <Container ID>:/home/carla/PythonAPI/carla/dist .
    ```

#### 1-2. Install Python library with `easy_intall`

Because `easy_install` has been removed after `setuptools 51.3.3`, we downgrade setuptools:

```bash
$ pip3 install setuptools==51.3.0
```

Then we can install Python library with `easy_install`

```bash
$ easy_install ./dist/carla-0.9.11-py3.7-linux-x86_64.egg
```

### 2. Running client example


```bash
$ git clone https://github.com/carla-simulator/carla.git
$ cd carla
```

#### Note: Checkout the git branch to the corresponding version

```bash
$ git checkout 0.9.11
```

Then, we can run the example

```bash
$ cd PythonAPI/examples/
$ python3 manual_control.py
```
