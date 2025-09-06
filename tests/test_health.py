import json
from app.main import app

def test_healthz():
    tester = app.test_client()
    response = tester.get("/healthz")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "ok"

