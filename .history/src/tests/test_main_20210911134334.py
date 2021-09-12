from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/PUT")
    assert response.status_code == 200
    assert response.json() == {
        "Message": "Hello wipro , This is a start to create a api"}
