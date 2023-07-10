# syntax=docker/dockerfile:1

# What base image to use for the application
FROM python:3.8-slim-buster

# Set Docker default location to this path
WORKDIR /app

# Copy our requirements.txt file into our Workding Directory /app
COPY requirements.txt ./requirements.txt

# Commands to run within our container
RUN apt-get update -y
RUN apt-get -y upgrade
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy source code files into our Working Directory
COPY . /app

# Execute our Python app within the container
CMD ["python3","pwgen.py"]
