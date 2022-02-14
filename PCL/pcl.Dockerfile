FROM ubuntu:18.04
LABEL maintainer="kaka <vn503024@gmail.com>"

# Ubuntu 18.04: tzdata issue
# set noninteractive installation
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    tzdata locales \
    wget curl ca-certificates \
	git build-essential linux-libc-dev \
	cmake ninja-build g++ \
    libxt-dev \
    libx11-dev libxext-dev libxtst-dev libxrender-dev libxmu-dev libxmuu-dev \
    libgl1-mesa-dev libglu1-mesa-dev \
    freeglut3-dev libboost-all-dev libeigen3-dev libflann-dev libglew-dev \
    libpcap-dev libusb-1.0-0-dev libopenni-dev libopenni2-dev clang-format libqhull-dev

# Install VTK
RUN apt-get install -y --no-install-recommends \
    libvtk6-dev \
    libvtk6-qt-dev

RUN apt -y autoremove && \
    apt -y autoclean && \
    apt -y clean && \
    rm -rf /var/lib/apt/lists/*

# Set timezone
RUN TZ=Asia/Taipei && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Set locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# PCL - build from source and install
RUN git clone https://github.com/PointCloudLibrary/pcl.git && \
    cd pcl && git checkout pcl-1.8.0 -b pcl-1.8.0 && \
    mkdir build && cd build && \
    cmake -DCMAKE_BUILD_TYPE=Release \
          -DBUILD_GPU=TRUE \
          -WITH_CUDA=FALSE \
          -DWITH_OPENGL=TRUE \
          -DWITH_QT=TRUE \
          -DWITH_VTK=TRUE \
          ..

RUN cd pcl/build && \
    make -j8 && \
    make install -j8 && \
    make clean

RUN rm -rf pcl

# nvidia-container-runtime
## can run OpenGL in Container
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# OpenGL
## This fix: libGL error: No matching fbConfigs or visuals found
ENV LIBGL_ALWAYS_INDIRECT 1
## To fix: QGLXContext: Failed to create dummy context
ENV QT_QUICK_BACKEND software

WORKDIR /root
