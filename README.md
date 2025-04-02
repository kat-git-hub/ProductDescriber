# AI Product Description Generator (Local LLM)

This is a simple AI-powered product description generator built with FastAPI and connected to a local LLM via [Ollama](https://ollama.com). It allows users to generate marketing-style product descriptions in different tones using models like Mistral, entirely offline and free.

---
[![Maintainability](https://qlty.sh/badges/54e1e6d9-8911-4ac3-8302-b22a0619fcd6/maintainability.svg)](https://qlty.sh/gh/kat-git-hub/projects/ProductDescriber)   [![Code Coverage](https://qlty.sh/badges/54e1e6d9-8911-4ac3-8302-b22a0619fcd6/test_coverage.svg)](https://qlty.sh/gh/kat-git-hub/projects/ProductDescriber)


## Features

- Input product details + select tone (e.g., friendly, technical, sales)
- Generates text using a local AI model
- Works with [Ollama](https://ollama.com) — no tokens, no limits
- Built with FastAPI + HTML/CSS
- Includes unit tests

---

## Tech Stack

- Python 3.12
- FastAPI
- Ollama (with `mistral` model)
- HTML + CSS
- Pytest for testing

---

## Setup & Run

1. Install Ollama
   → [https://ollama.com/download](https://ollama.com/download)

2. Run Ollama server (in one terminal):
```
ollama serve
```
3.  Install dependencies with Poetry
```
poetry install
```
4. Start the FastAPI app
```
make runserver
```

Then open in browser:
http://127.0.0.1:8000

5.  Run tests
```
make test
```
