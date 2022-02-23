#!/bin/bash

mkdir -p build && cd build
cmake -G Ninja -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .

cp cv_example.*.so ../cv_example.so
