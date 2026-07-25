from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_system_info():
    response = client.get("/system/info")
    assert response.status_code == 200