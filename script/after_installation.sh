#!/usr/bin/env bash

source /var/lib/jenkins/workspace/game_pipeline/game-venv/bin/activate

cd  /var/lib/jenkins/workspace/game_pipeline


source ~/.bashrc

gunicorn --workers=4 --bind=0.0.0.0:5000 application:app