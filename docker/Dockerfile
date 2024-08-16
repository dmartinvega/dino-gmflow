FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

RUN apt update && apt upgrade
RUN apt-get update && apt-get install git ffmpeg libsm6 libxext6 libgl1 curl -y
EXPOSE 4000 

RUN apt-get install libgl1 libglib2.0-0 libsm6 libxrender1 libxext6
