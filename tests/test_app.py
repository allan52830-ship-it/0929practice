import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Flask" in response.data.decode("utf-8")
    assert "你好，世界" in response.data.decode("utf-8")
