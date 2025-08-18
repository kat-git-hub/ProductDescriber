IMAGE       ?= productdescriber:latest
CONTAINER   ?= productdescriber
PORT        ?= 8000
ENV_FILE    ?= .env
OLLAMA_URL  ?= http://host.docker.internal:11434

install:
	poetry install --no-root
lint:
	poetry run flake8 productdescriber tests --ignore=E501
pre-commit:
	poetry run pre-commit run --all-files
runserver:
	uvicorn productdescriber.main:app --reload
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=productdescriber --cov-branch \
	  --cov-report=term-missing:skip-covered \
	  --cov-report=xml:coverage.xml
docker-build:
	docker build -t $(IMAGE) .
docker-run:
	docker run -d --rm --name $(CONTAINER) -p $(PORT):8000 \
	  --env-file $(ENV_FILE) \
	  -e OLLAMA_URL=$(OLLAMA_URL) \
	  $(IMAGE)
docker-stop:
	- docker stop $(CONTAINER)
compose-up:
	docker compose up --build
compose-down:
	docker compose down
