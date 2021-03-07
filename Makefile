tests:
	pushd core &&\
	pytest &&\
	popd

test: tests

t: tests

run:
	python core/manage.py runserver

r: run

setup:
	pipenv install --dev
	pipenv run python core/manage.py migrate
	pipenv run make tests
	pipenv shell

s: setup
