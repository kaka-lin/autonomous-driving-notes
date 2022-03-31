#!/bin/bash

xhost +local:root
if [ "$1" = "python" ]; then
    docker run --rm -it \
        --gpus all \
        -e DISPLAY=$DISPLAY \
        -e QT_X11_NO_MITSHM=1 \
        --volume="$PWD:/root/PCL" \
        --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
        --privileged \
        kakalin/python-pcl:1.8.0
else
    docker run --rm -it \
        --gpus all \
        -e DISPLAY=$DISPLAY \
        -e QT_X11_NO_MITSHM=1 \
        --volume="$PWD:/root/PCL" \
        --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
        --privileged \
        kakalin/pcl:1.8.0
fi
