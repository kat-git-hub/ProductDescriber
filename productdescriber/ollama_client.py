from typing import Any, Dict
import requests
from starlette.concurrency import run_in_threadpool
from .settings import OLLAMA_URL, MODEL_NAME, NUM_PREDICT, KEEP_ALIVE, HTTP_TIMEOUT, NUM_THREAD, NUM_CTX


def _post_generate(payload: Dict[str, Any]) -> Dict[str, Any]:
    url = f"{OLLAMA_URL.rstrip('/')}/api/generate"
    r = requests.post(url, json=payload, timeout=HTTP_TIMEOUT)
    try:
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        detail = ""
        try:
            detail = r.text
        except Exception:
            pass
        raise requests.HTTPError(f"{e} | body: {detail}") from e


async def generate(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "keep_alive": KEEP_ALIVE,
        "options": {
            "num_predict": NUM_PREDICT,
            "num_ctx": NUM_CTX,
            "num_thread": NUM_THREAD,
        },
    }
    data = await run_in_threadpool(_post_generate, payload)
    return data.get("response", "No response from the model")
