#!/usr/bin/env bash


sudo cp etc/systemd/system/flask.service /etc/systemd/system

sudo systemctl daemon-reload

sudo systemctl enable flask.service

source game-venv/bin/activate

sudo systemctl start flask.service

pip3 install -r /var/lib/jenkins/workspace/game_pipeline/requirements.txt

