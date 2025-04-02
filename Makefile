install:
	poetry install --no-root
lint:
	poetry run flake8 main.py --ignore=E501
pre-commit:
	poetry run pre-commit run --all-files
runserver:
	uvicorn main:app --reload
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=main --cov-report=xml
