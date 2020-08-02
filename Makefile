build:
	docker-compose build
up:
	docker-compose up
d:
	docker-compose up --detach
rm:
	docker-compose rm --force
admin:
	docker-compose exec application python /app/manage.py createsuperuser --username admin --email ""
