# base image
FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# copy requirements.txt
COPY requirements.txt /code/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /code/