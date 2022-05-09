#!/bin/bash

xhost +local:root
docker run --rm -it \
    --gpus all \
    -e DISPLAY=$DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    --volume="$PWD:/root/project" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    kakalin/pcl:1.8.0
