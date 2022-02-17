#!/bin/bash

SECRET=$(python -c 'import secrets; print(secrets.token_hex())')
echo "SECRET=${SECRET}" >> /api/instance/config.py
echo "MYSQL_HOST=${MYSQL_HOST}" >> /api/instance/config.py
echo "MYSQL_PORT=${MYSQL_PORT}" >> /api/instance/config.py
echo "MYSQL_USER=${MYSQL_USER}" >> /api/instance/config.py
echo "MYSQL_PASSWORD=${MYSQL_PASSWORD}" >> /api/instance/config.py
echo "MYSQL_DATABASE=${MYSQL_DATABASE}" >> /api/instance/config.py

waitress-serve --call whatsin:create_app