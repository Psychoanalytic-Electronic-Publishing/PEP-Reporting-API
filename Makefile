.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

python-packages:
	pip install -r requirements.txt --upgrade

install: python-packages

tests:
	python -m pytest

run:
	python manage.py run

all: clean install tests run
