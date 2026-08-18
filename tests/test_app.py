from app.app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "running"
    assert data["message"] == "GitHub Actions Security Hardening Demo"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
