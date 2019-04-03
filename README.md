# homography_estimation
Ongoing project to estimate homography in various scenes. Currently, the goal is to develop a tool to estimate the homography of various sports fields from images to top-down viewpoint.

## Building and Running
Dependencies:
- Docker

### Running to annotate
Clone git repo

    git clone https://github.com/neherh/homography_estimation.git

run in the cloned directory:

    docker build -t computer_vision .

once built run using:

    xhost +
    docker run --rm -ti --net=host --ipc=host    -e DISPLAY=$DISPLAY    -v /tmp/.X11-unix:/tmp.X11-unix    computer_vision python homography_estimation.py

### Editing the python scripts:
Clone git repo:

    git clone https://github.com/neherh/homography_estimation.git

Edit the Dockerfile and comment out the line: 
    
    COPY . /app

run in the cloned directory:

    docker build -t computer_vision .

once built run using:
    
    xhost +
    ****docker run --rm -ti --net=host --ipc=host    -e DISPLAY=$DISPLAY    -v /tmp/.X11-unix:/tmp.X11-unix    computer_vision python homography_estimation.py

docker-compose build
docker-compose run --rm app




xhost is needed to view the gui.

