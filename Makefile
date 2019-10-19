ACTIVATE = source .venv/bin/activate &&

all:
	make venv
	make npm
	make build_game_configs

start:
	$(ACTIVATE) python manage.py runserver

npm:
	@npm ci

watch:
	make watch_css & make watch_js

watch_js:
	@npm run watch:js

watch_css:
	@npm run watch:css

npm_install:
	@npm ci

npm_lock:
	@npm install

build_game_configs:
	$(ACTIVATE) python manage.py shell < compile_configs.py

clean_data:
	$(ACTIVATE) python manage.py flush

venv:
	python3 -m venv .venv
	$(ACTIVATE) pip install -r requirements.txt
