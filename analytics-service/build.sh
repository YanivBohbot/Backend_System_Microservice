#!/bin/bash

docker login
docker build --tag yanivbohbot/analytics:v1.0.0 . -f Dockerfile
docker push yanivbohbot/analytics:v1.0.0