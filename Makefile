SHELL := /bin/bash

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf .pytest_cache
	rm -rf db.sqlite3
	rm -rf web/.pytest_cache

test:
	python manage.py test

up:
	docker compose up -d

build:
	docker compose build

stop:
	docker compose stop

re:
	docker compose restart

exp:
	export DB_NAME=cars_city
	export DB_USER=postgres
	export DB_PASSWORD=postgres
	export DB_HOST=172.18.0.2
	export DB_PORT=5432