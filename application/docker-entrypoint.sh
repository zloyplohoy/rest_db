#!/bin/bash

set -e
/app/wait-for-it.sh $DB_HOST:$DB_PORT
python /app/manage.py migrate --noinput
python /app/manage.py runserver 0.0.0.0:8000
