import productdescriber.routes as routes


def test_get_form(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert "<form" in resp.text


def test_generate_success(client, monkeypatch):
    async def fake_generate_description(product: str, style: str) -> str:
        assert product == "Thermal mug 500ml"
        assert style == "friendly"
        return "This is a test product description."

    # Patch the exact name imported in routes.py
    monkeypatch.setattr(routes, "generate_description", fake_generate_description)

    resp = client.post(
        "/generate",
        data={"product": "Thermal mug 500ml", "style": "friendly"},
    )
    assert resp.status_code == 200
    assert "This is a test product description." in resp.text


def test_generate_error_path(client, monkeypatch):
    async def fake_generate_description(product: str, style: str) -> str:
        raise RuntimeError("boom")

    monkeypatch.setattr(routes, "generate_description", fake_generate_description)

    resp = client.post("/generate", data={"product": "X", "style": "Y"})
    assert resp.status_code == 200
    assert "Error:" in resp.text
