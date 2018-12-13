# secam

## Camera

## Docker on Raspberry Pi
Docker installation

	curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

Alternative installation command: curl -sSL https://get.docker.com | sh

Docker Compose installation:

	sudo pip install docker-compose

Post installation steps: https://docs.docker.com/install/linux/linux-postinstall/

References:

https://medium.freecodecamp.org/the-easy-way-to-set-up-docker-on-a-raspberry-pi-7d24ced073ef

## Tensorflow
### Image
Publish images to Docker

Build image

	docker build -t rpi-tensorflow .

Run image

	docker run --name tfinstance -p 8888:8888 -d rpi-tensorflow
	
	# Send video stream to image: docker run --device=/dev/video0

### Model
References:

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi

## Node-RED