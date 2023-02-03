# pull official base image
FROM python:3.10.7-buster

RUN apt-get update
RUN apt-get install -y supervisor

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY supervisord.conf /etc/


RUN pip3 install --upgrade pip
RUN pip3 install waitress
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# install dependencies
COPY . /usr/src/app/
RUN pip3 install -e .
EXPOSE 5000

CMD ["/usr/bin/supervisord"]
