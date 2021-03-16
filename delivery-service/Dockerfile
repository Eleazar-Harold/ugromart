FROM python:3.8-slim

LABEL maintainer="eleazar.yewa.harold@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /app/
