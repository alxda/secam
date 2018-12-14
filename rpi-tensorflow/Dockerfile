# tensorflow on raspbian

FROM resin/rpi-raspbian

# install tensorflow
RUN sudo apt update
RUN sudo apt install python3-dev python3-pip
RUN	sudo apt install libatlas-base-dev # required for numpy
RUN	sudo pip3 install -U virtualenv # system-wide install

RUN pip3 --no-cache-dir install --upgrade pip setuptools

# RUN	pip install --upgrade tensorflow
# RUN pip3 install --user --upgrade tensorflow  # install in $HOME
RUN pip3 install tensorflow

# install tensorflow object detection api
RUN pip3 install --user Cython && \
	pip3 install --user contextlib2 && \
	pip3 install --user pillow && \
	pip3 install --user lxml && \
	pip3 install --user jupyter && \
	pip3 install --user matplotlib

RUN mkdir -p /tensorflow/models
RUN git clone https://github.com/tensorflow/models.git /tensorflow/models

## install protobuf
WORKDIR /tensorflow/models/research

RUN wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
RUN unzip protobuf.zip
RUN ./bin/protoc object_detection/protos/*.proto --python_out=.


RUN export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

# References:
# https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/docker
# https://www.tensorflow.org/install/pip
# https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
# https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi#4-compile-and-install-protobuf