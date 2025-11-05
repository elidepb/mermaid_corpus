from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Mermaid Diagram Viewer" in response.text

def test_read_diagram():
    response = client.get("/diagrams/045")
    assert response.status_code == 200
    assert "Systems Engineering" in response.text
