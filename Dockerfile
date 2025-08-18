FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN pip install --no-cache-dir "poetry>=2.0,<3.0"

COPY pyproject.toml poetry.lock* ./
RUN poetry install --only main --no-interaction --no-ansi --no-root \
  && pip uninstall -y poetry


COPY productdescriber ./productdescriber
COPY templates ./templates
COPY static ./static

EXPOSE 8000
CMD ["uvicorn", "productdescriber.main:app", "--host", "0.0.0.0", "--port", "8000"]
