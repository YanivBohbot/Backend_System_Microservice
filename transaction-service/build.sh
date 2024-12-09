#!/bin/bash

docker login
docker build --tag yanivbohbot/transactions:v1.0.0 . -f Dockerfile
docker push yanivbohbot/transactions:v1.0.0