#!/usr/bin/env bash

source /var/lib/jenkins/workspace/game_pipeline/exportvariables

export DATABASE_URI="mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOST}/${MYSQL_DATABASE}"

export SECRET_KEY=${SECRET_KEY}