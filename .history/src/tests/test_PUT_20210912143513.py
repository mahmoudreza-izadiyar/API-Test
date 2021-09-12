from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_PUT(test_app):
    response = test_app.get("/PUT")
    assert response.status_code == 200
    assert response.json() == {
        "Message": "Hello wipro , This is a start to create a api"}
