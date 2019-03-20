# homography_estimation
Ongoing project to estimate homography in various scenes. Currently, the goal is to develop a tool to estimate the homography of various sports fields from images to top-down viewpoint.

Dependencies:
- Docker

Clone git repo

run in the cloned file:
docker build -t computer_vision .

once built run using:
$ xhost +
$ docker run --rm -ti --net=host --ipc=host    -e DISPLAY=$DISPLAY    -v /tmp/.X11-unix:/tmp.X11-unix    computer_vision python homography_estimation.py


xhost is needed to view the gui.

