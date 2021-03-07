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
	pipenv shell
	tests
	run

s: setup
