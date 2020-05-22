#!/usr/bin/env bash

sudo apt update -y

sudo apt install python3 -y

sudo apt install python3-pip -y

sudo apt install python3-venv -y

python3 -m venv game-venv

source game-venv/bin/activate

pip3 install -r /var/lib/jenkins/workspace/game_freestyle/requirements.txt

pytest --cov ./application --cov-report html

source ~/.bashrc

python3 /var/lib/jenkins/workspace/game_freestyle/app.py