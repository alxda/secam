# secam

## Camera

## Docker on Raspberry Pi
Installation

	curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

Alternative command:

	curl -sSL https://get.docker.com | sh

References:

https://medium.freecodecamp.org/the-easy-way-to-set-up-docker-on-a-raspberry-pi-7d24ced073ef

## Tensorflow Image
Publish images to Docker

Build image

	docker build -t rpi-tensorflow .

Run image

	docker run --name tfinstance -p 8888:8888 -d rpi-tensorflow
	
	# Send video stream to image: docker run --device=/dev/video0

## Tensorflow Model
References:

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi

## Node-RED
