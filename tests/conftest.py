from fastapi.testclient import TestClient
import pytest
from productdescriber.main import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
