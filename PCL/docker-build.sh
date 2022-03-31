#!/bin/bash

cd 00_installation
if [ "$1" = "python" ]; then
    docker build --rm \
        -t kakalin/python-pcl:1.8.0 \
        -f python-pcl.Dockerfile .
else
    docker build --rm \
        -t kakalin/pcl:1.8.0 \
        -f pcl.Dockerfile .
fi
