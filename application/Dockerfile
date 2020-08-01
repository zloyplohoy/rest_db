FROM python:3.8.5

COPY docker-entrypoint.sh \
     src/requirements.txt \
     wait-for-it/wait-for-it.sh \
     /app/

RUN pip install -r /app/requirements.txt

COPY src  /app
