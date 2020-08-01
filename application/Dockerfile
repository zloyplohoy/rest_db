FROM python:3.8.5

COPY src/requirements.txt  /app/

RUN pip install -r /app/requirements.txt

COPY src \
     docker-entrypoint.sh \
     wait-for-it/wait-for-it.sh \
     /app/

RUN python /app/manage.py collectstatic --noinput
