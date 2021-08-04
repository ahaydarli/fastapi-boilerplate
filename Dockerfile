FROM library/python:3.7-slim

MAINTAINER ali

RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
