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

