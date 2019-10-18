ACTIVATE = source .venv/bin/activate &&

all:
	make venv
	make npm
	make build_game_configs

start:
	$(ACTIVATE) python manage.py runserver

npm:
	cd static/js/;\
	npm ci

build_game_configs:
	$(ACTIVATE) python manage.py shell < compile_configs.py

clean_data:
	$(ACTIVATE) python manage.py flush

build_static:
	sass static/scss/base.scss static/css/main.css
	browserify static/js/main.js > static/js/bundle.js

venv:
	python3 -m venv .venv
	$(ACTIVATE) pip install -r requirements.txt
