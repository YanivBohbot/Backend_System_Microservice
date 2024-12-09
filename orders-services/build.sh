#!/bin/bash

docker login
docker build --tag yanivbohbot/orders:v1.0.0 . -f Dockerfile
docker push yanivbohbot/orders:v1.0.0