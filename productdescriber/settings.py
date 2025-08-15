import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "mistral")
NUM_PREDICT = int(os.getenv("NUM_PREDICT", "120"))
NUM_CTX = int(os.getenv("NUM_CTX", "2048"))
NUM_THREAD = int(os.getenv("NUM_THREAD", "4"))
KEEP_ALIVE = os.getenv("KEEP_ALIVE", "10m")
HTTP_TIMEOUT = int(os.getenv("HTTP_TIMEOUT", "120"))
