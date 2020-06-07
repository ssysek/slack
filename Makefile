.PHONY: run
run:
	pipenv run python slack_server.py

.PHONY: install
install:
	pip install pipenv; \
	pipenv install; \
	pipenv install --dev