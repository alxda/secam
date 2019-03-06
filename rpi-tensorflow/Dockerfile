# tensorflow on raspbian

FROM resin/rpi-raspbian:stretch

# Install tensorflow
RUN sudo apt update
RUN sudo apt install python3-dev python3-pip python3-setuptools
RUN	sudo apt install libatlas-base-dev # required for numpy

RUN sudo pip3 install --upgrade pip
RUN	sudo pip3 install -U virtualenv # system-wide install

RUN python3 --version && \
    pip3 --version && \
    virtualenv --version

RUN mkdir ~/secamdir && \
    cd ~/secamdir && \
    virtualenv --system-site-packages -p python3 ./secamenv

# Alternative: RUN source secamenv/bin/activate
# RUN . secamenv/bin/activate
RUN /bin/bash source secamenv/bin/activate

RUN python --version

# RUN pip3 install --user --upgrade tensorflow  # install in $HOME
RUN sudo pip install --upgrade tensorflow

# install tensorflow object detection api
RUN sudo apt-get update
RUN sudo apt-get upgrade
RUN sudo apt-get install git g++ protobuf-compiler python-pil python-lxml python-tk python3-matplotlib
RUN sudo pip install Cython
RUN	sudo pip install contextlib2
RUN	sudo pip install jupyter

RUN mkdir -p /tensorflow/models
RUN git clone https://github.com/tensorflow/models.git /tensorflow/models

# Install protobuf
WORKDIR /tensorflow/models/research

# RUN wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
# RUN unzip protobuf.zip
RUN protoc object_detection/protos/*.proto --python_out=.

RUN export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

WORKDIR /root/secamdir
# Install secam python script
# Copy python script to target image
RUN mkdir ./scripts
COPY rpi-tensorflow/*.py ./scripts/
# Install script specific python modules
RUN sudo apt-get install python-opencv python-six
RUN sudo pip list
RUN python3 -u ./scripts/checkDependencies.py
RUN python3 -u ./scripts/objectDetection.py

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

# References:
# https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/docker
# https://www.tensorflow.org/install/pip
# https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
# https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi#4-compile-and-install-protobuf