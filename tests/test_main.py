from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_form():
    response = client.get("/")
    assert response.status_code == 200
    assert "<form" in response.text


def test_generate_description(monkeypatch):
    # mock Ollama API response
    def mock_post(*args, **kwargs):
        class MockResponse:
            def json(self):
                return {"response": "This is a test product description."}

        return MockResponse()

    import main

    monkeypatch.setattr(main.requests, "post", mock_post)

    response = client.post(
        "/generate",
        data={
            "product": "Thermal mug 500ml, keeps warm for 12 hours",
            "style": "friendly",
        },
    )

    assert response.status_code == 200
    assert "This is a test product description." in response.text
