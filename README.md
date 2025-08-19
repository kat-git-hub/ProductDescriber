# AI Product Description Generator (Local LLM)

This is a simple AI-powered product description generator built with FastAPI and connected to a local LLM via [Ollama](https://ollama.com). It allows users to generate marketing-style product descriptions in different tones using models like Mistral, entirely offline and free.

---
[![Maintainability](https://qlty.sh/badges/54e1e6d9-8911-4ac3-8302-b22a0619fcd6/maintainability.svg)](https://qlty.sh/gh/kat-git-hub/projects/ProductDescriber)   [![Code Coverage](https://qlty.sh/badges/54e1e6d9-8911-4ac3-8302-b22a0619fcd6/test_coverage.svg)](https://qlty.sh/gh/kat-git-hub/projects/ProductDescriber)   [![CI](https://github.com/kat-git-hub/ProductDescriber/actions/workflows/CI.yml/badge.svg)](https://github.com/kat-git-hub/ProductDescriber/actions/workflows/CI.yml)


## Features

- Input product details + select tone (e.g., friendly, technical, sales)
- Generates text using a local AI model
- Works with [Ollama](https://ollama.com) — no tokens, no limits
- Built with FastAPI + HTML/CSS
- Includes unit tests

---

## Tech Stack

- Python 3.10+
- FastAPI + Uvicorn
- Ollama (with `mistral` model)
- HTML + CSS
- Jinja2, python-dotenv
- Pytest

---

## Setup & Run

### Run locally (Poetry)

1. Clone
```
git clone https://github.com/kat-git-hub/ProductDescriber.git
cd ProductDescriber
```
2.  Install dependencies with Poetry
```
poetry install
```
3. Ollama: start & pull a model
```
ollama serve                    # if not running as a service
ollama pull mistral             # or: ollama pull llama3.2:3b
ollama list                     # verify the model is available
```
4. Start the FastAPI app
```
poetry run uvicorn productdescriber.main:app --reload
```
or, if you use Makefile:
```
make runserver
```

Then open in browser:
http://127.0.0.1:8000

5.  Run tests
```
poetry run pytest -vv

or:

make test
```

### Run with Docker

1. Build the image:
```
docker build -t productdescriber:latest .

or:

make docker-build
```
2. Run the container (macOS/Windows — Ollama on the host):
```
docker run --rm -p 8000:8000 \
  -e OLLAMA_URL=http://host.docker.internal:11434 \
  -e MODEL_NAME=mistral \
  productdescriber:latest

or:

make docker-run
```

3. Open: http://localhost:8000

4. Stop the container:
```
docker stop productdescriber

or:

make docker-stop
```