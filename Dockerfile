# Use an official Python runtime as a parent image
FROM jjanzic/docker-python3-opencv

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Various Python and C/build deps
#RUN apt-get update && apt-get install -y \ 
#    wget \
#    python-opencv




# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Define environment variable
ENV NAME World

# Run app.py when the container launches
#CMD ["python", "homography_estimation.py"]
