#!/bin/bash

source ./BotEnv/bin/activate
echo 'Virtual Environment Activated'

python bot.py "$1"
echo 'Bot Started!'