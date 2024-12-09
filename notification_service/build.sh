#!/bin/bash

docker login
docker build --tag yanivbohbot/notification:v1.0.0 . -f Dockerfile
docker push yanivbohbot/notification:v1.0.0