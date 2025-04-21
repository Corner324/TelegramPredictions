#!/bin/bash

source ./BotEnv/bin/activate
echo 'Virtual Environment Activated'

docker build -t prediction . && docker run -p 8000:80 -v "$PWD":/app prediction
echo 'Bot Started!'