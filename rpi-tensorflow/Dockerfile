# tensorflow on raspbian

FROM resin/rpi-raspbian

# install tensorflow
RUN sudo apt update && \
	sudo apt install python3-dev python3-pip && \
	sudo apt install libatlas-base-dev && \ # required for numpy
	sudo pip3 install -U virtualenv # system-wide install

RUN	pip install --upgrade tensorflow

# install tensorflow object detection api
RUN pip install --user Cython && \
	pip install --user contextlib2 && \
	pip install --user pillow && \
	pip install --user lxml && \
	pip install --user jupyter && \
	pip install --user matplotlib

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