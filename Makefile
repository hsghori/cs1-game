ACTIVATE = source .venv/bin/activate &&

all:
	make venv
	make npm

start:
	$(ACTIVATE) python manage.py runserver

npm:
	cd static/js/;\
	npm ci

build_static:
	sass static/scss/base.scss static/css/main.css
	browserify static/js/main.js > static/js/bundle.js

venv:
	python3 -m venv .venv
	$(ACTIVATE) pip install -r requirements.txt
