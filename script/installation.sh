#!/usr/bin/env bash

sudo apt update -y

sudo apt install python3 -y

sudo apt install python3-pip -y

sudo apt install python3-venv -y

python3 -m venv game-venv

source game-venv/bin/activate

pip3 install -r /var/lib/jenkins/workspace/game_freestyle/requirements.txt

pip3 install gunicorn

pip3 install pytest pytest-cov flask-testing Werkzeug==0.16.1

python3 pytest --cov ./application --cov-report html

source ~/.bashrc

gunicorn --workers=4 --bind=0.0.0.0:5000 /var/lib/jenkins/workspace/game_freestyle/application:app