# tensorflow on raspbian

FROM balenalib/raspberrypi3-debian
# FROM arm32v7/debian

RUN cat /etc/*-release

RUN apt-get update && apt-get install -y \
    python3 python3-dev python3-pip libatlas-base-dev

RUN pip3 --no-cache-dir install --upgrade pip setuptools

# Some TF tools expect a "python" binary
RUN ln -s python3 /usr/local/bin/python

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    wget \
    openjdk-8-jdk \
    swig

# Install tensorflow
RUN sudo pip3 install -U virtualenv # system-wide install

RUN python3 --version && \
    pip3 --version

# RUN python3 -c "import pip._internal; print(pip._internal.pep425tags.get_supported())"

RUN mkdir /secamdir && \
    cd /secamdir && \
    virtualenv --system-site-packages -p python3 ./secamenv && \
    /bin/bash -c  "source ./secamenv/bin/activate"

RUN pip --version

RUN pip install --upgrade tensorflow

RUN pip list #show packages installed within the virtual environment

RUN python3 -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"

# install tensorflow object detection api

RUN sudo apt-get update && \
    sudo apt-get upgrade && \
    sudo apt-get install git g++ protobuf-compiler python-pil python-lxml python-tk python3-matplotlib && \
    sudo pip install Cython contextlib2 jupyter

RUN mkdir -p /tensorflow/models
RUN git clone https://github.com/tensorflow/models.git /tensorflow/models

# Install protobuf
WORKDIR /tensorflow/models/research

# RUN wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
# RUN unzip protobuf.zip
RUN protoc object_detection/protos/*.proto --python_out=.

# RUN export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
RUN echo "export PYTHONPATH=${PYTHONPATH}:`pwd`:`pwd`/slim" >> ~/.bashrc

WORKDIR /secamdir
# Install secam python script
# Copy python script to target image
RUN mkdir ./scripts
COPY . ./scripts/
# Install script specific python modules (e.g. opencv)
RUN sudo apt-get install python3-numpy python-six python3-opencv libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test && \
    sudo pip install Pillow && \
    sudo pip list

WORKDIR /secamdir
RUN python3 -u ./scripts/checkDependencies.py && \
    python3 -u ./scripts/objectDetection.py

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

# References:
# https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/docker
# https://www.tensorflow.org/install/pip
# https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
# https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi#4-compile-and-install-protobuf
# https://circuitdigest.com/microcontroller-projects/how-to-install-python-opencv-on-raspberry-pi