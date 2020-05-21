#!/usr/bin/env bash

sudo apt update -y

sudo apt install python3 -y

sudo apt install python3-pip -y

sudo apt install python3-venv -y

python3 -m venv game-venv

source /var/lib/jenkins/workspace/game_freestyle/game-venv/bin/activate

pip3 install -r requirements.txt

export SECRET_KEY=sdfjsfjsngjdfrj

export DATABASE_URI=mysql+pymysql://root:1234@34.89.55.147/gamedatabase

python3 /var/lib/jenkins/workspace/game_freestyle/app.py