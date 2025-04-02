install:
	poetry install
lint:
	poetry run flake8 app --ignore=E501
pre-commit:
	poetry run pre-commit run --all-files
runserver:
	uvicorn main:app --reload
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=main --cov-report=xml
