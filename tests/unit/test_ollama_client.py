import pytest
import requests
from productdescriber.ollama_client import generate


class _RespOK:
    status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return {"response": "HELLO"}


class _RespErr:
    status_code = 500

    def raise_for_status(self):
        raise requests.HTTPError("server error")

    def json(self):
        return {}


@pytest.mark.asyncio
async def test_client_success(monkeypatch):
    def fake_post(*args, **kwargs):
        return _RespOK()
    monkeypatch.setattr(requests, "post", fake_post)

    out = await generate("prompt")
    assert out == "HELLO"


@pytest.mark.asyncio
async def test_client_http_error(monkeypatch):
    def fake_post(*args, **kwargs):
        return _RespErr()
    monkeypatch.setattr(requests, "post", fake_post)

    with pytest.raises(requests.HTTPError):
        await generate("prompt")
