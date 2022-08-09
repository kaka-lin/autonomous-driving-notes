#!/bin/bash

xhost +local:root
docker run \
    -it \
    --gpus all \
    -e DISPLAY=$DISPLAY \
	-e QT_X11_NO_MITSHM=1 \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    --network=host \
    --shm-size="20g" \
    --volume="$PWD:/root/project/" \
    kakalin/pcl:1.8.0
