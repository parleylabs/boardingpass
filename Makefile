.PHONY: makemigrations
makemigrations:
	@docker-compose run --rm api python ./manage.py makemigrations

.PHONY: migrate
migrate:
	@docker-compose run --rm api python ./manage.py migrate

.PHONY: createsuperuser
createsuperuser:
	@docker-compose run --rm api python ./manage.py createsuperuser