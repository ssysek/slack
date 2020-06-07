.PHONY: run
run:
	pipenv run python slack_server.py & \
	pipenv run python landingpage_new.py


.PHONY: install
install:
	pip install pipenv; \
	pipenv install; \
	pipenv install --dev