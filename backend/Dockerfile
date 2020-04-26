# pull official base image
FROM tiangolo/meinheld-gunicorn-flask:python3.7

# Create a directory where our app will be placed
RUN mkdir -p /usr/src/app/

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN apt-get update && apt-get -y install cmake
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

EXPOSE 3008/tcp