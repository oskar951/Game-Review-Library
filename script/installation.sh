#!/usr/bin/env bash

sudo apt update -y

sudo apt install python3 -y

sudo apt install python3-pip -y

sudo apt install python3-venv -y

python3 -m venv game-venv

source /var/lib/jenkins/workspace/game_freestyle/game-venv/bin/activate

pip3 install -r /var/lib/jenkins/workspace/game_freestyle/requirements.txt

cd  /var/lib/jenkins/workspace/game_freestyle

pytest --cov ./application --cov-report html


source ~/.bashrc

gunicorn --workers=4 --bind=0.0.0.0:5000 application:app