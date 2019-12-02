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

## GitLab Runner on Raspberry Pi

Share Runners of gitlab.com support only the x86 architecture. Building for arm will therefore fail at some point eventually. Therefore, a runner needs to be installed on the Raspberry Pi and registered to gitlab.com. The standard gitlab/gitlab-runner docker image doesn't work, however, on arm. Use instead the image provided by klud.  

References:

https://hub.docker.com/r/klud/gitlab-runner/

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

## Continuous Deployment

Start current version of images as containers on the raspberry

Use watchtower to update and restart the containers each time a new version of the images are published to docker hub.

## Outlook
Ocean Protocol, BigchainDB

References:

https://github.com/v2tec/watchtower
