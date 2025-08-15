import pytest
import productdescriber.generator as generator
import productdescriber.ollama_client as ollama_client
from productdescriber.generator import build_prompt, generate_description


def test_build_prompt():
    p = build_prompt("Thermal mug 500ml", "friendly")
    assert "friendly" in p and "Thermal mug 500ml" in p


@pytest.mark.asyncio
async def test_generate_description_success(monkeypatch):
    async def fake_generate(prompt: str) -> str:
        return "OK"

    monkeypatch.setattr(generator, "ollama_generate", fake_generate, raising=False)
    monkeypatch.setattr(ollama_client, "generate", fake_generate, raising=False)

    out = await generate_description("A", "B")
    assert out == "OK"


@pytest.mark.asyncio
async def test_generate_description_error(monkeypatch):
    async def fake_generate(_prompt: str) -> str:
        raise RuntimeError("boom")

    monkeypatch.setattr(generator, "ollama_generate", fake_generate, raising=False)
    monkeypatch.setattr(ollama_client, "generate", fake_generate, raising=False)

    with pytest.raises(RuntimeError):
        await generate_description("A", "B")
