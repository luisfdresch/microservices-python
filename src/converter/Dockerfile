# Define a build argument for the base image
ARG BASE_IMAGE=python:3.10-slim-bullseye

# Use the base image argument
FROM ${BASE_IMAGE}

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential ffmpeg \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

CMD ["python3", "consumer.py"]
