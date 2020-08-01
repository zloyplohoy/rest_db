#!/bin/bash
/app/wait-for-it $DB_HOST:$DB_PORT

python /app/manage.py migrate

python /app/manage.py runserver
