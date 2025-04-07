from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Faleproxy"}

def test_proxy_no_url():
    response = client.get("/proxy")
    assert response.status_code == 422  # FastAPI validation error

def test_proxy_with_url():
    test_url = "https://httpbin.org/get"
    response = client.get(f"/proxy?url={test_url}")
    assert response.status_code == 200
    data = response.json()
    assert "status_code" in data
    assert "headers" in data
    assert "content" in data
