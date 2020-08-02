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
migrations:
	export $(cat application.env | xargs) && export DB_HOST=localhost && application/src/manage.py makemigrations
