all:
	make python_install
	make npm_install
	make build_static
	make build_game_configs
	make make_migrations
	make migrate

start:
	@docker-compose up

build:
	@docker-compose build

shell:
	@docker exec -ti game bash

migrate:
	python manage.py migrate

make_migrations:
	python manage.py makemigrations

watch:
	make watch_css & make watch_js

watch_js:
	@npm run watch:js

watch_css:
	@npm run watch:css

build_static:
	@npm run build:js
	@npm run build:css

python_install:
	@pip install -r requirements.txt

npm_install:
	@npm ci

npm_lock:
	@npm install

build_game_configs:
	python manage.py shell < compile_configs.py

clean_data:
	python manage.py flush
