FROM ubuntu:18.04
LABEL maintainer="kaka <vn503024@gmail.com>"

# Ubuntu 18.04: tzdata issue
# set noninteractive installation
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    tzdata locales \
    wget curl ca-certificates \
	git build-essential \
    python-dev python3-dev \
    python-pip python3-pip \
    libpcl-dev

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

# Install Python Packages
RUN pip3 install --upgrade pip
RUN pip3 install setuptools numpy cython==0.25.2

# Install python-pcl
RUN wget https://github.com/strawlab/python-pcl/archive/v0.3.0rc1.tar.gz
RUN tar zxvf v0.3.0rc1.tar.gz
WORKDIR /python-pcl-0.3.0rc1
COPY python-pcl/setup.py .
RUN python3 setup.py build_ext -i
RUN python3 setup.py install
WORKDIR /
RUN rm v0.3.0rc1.tar.gz && rm -r /python-pcl-0.3.0rc1

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
