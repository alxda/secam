# tensorflow on raspbian

FROM resin/rpi-raspbian

RUN sudo apt update &&
	sudo apt install python3-dev python3-pip &&
	sudo apt install libatlas-base-dev && # required for numpy
	sudo pip3 install -U virtualenv # system-wide install

RUN	pip install --upgrade tensorflow

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

# References:
# https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/docker
# https://www.tensorflow.org/install/pip