#!/bin/bash

SECRET=$(python -c 'import secrets; print(secrets.token_hex())')
CONFIG='/app/instance/config.py'

echo "SECRET='${SECRET}'" >> $CONFIG
echo "MYSQL_HOST='${MYSQL_HOST}'" >> $CONFIG
echo "MYSQL_PORT='${MYSQL_PORT}'" >> $CONFIG
echo "MYSQL_USER='${MYSQL_USER}'" >> $CONFIG
echo "MYSQL_DATABASE='${MYSQL_DATABASE}'" >> $CONFIG
echo "MYSQL_PASSWORD='${MYSQL_PASSWORD}'" >> $CONFIG

gunicorn --chdir /app whatsin:app -b 0.0.0.0:8080
