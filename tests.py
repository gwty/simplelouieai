from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)

def test_invalid_file():
    response = client.post("/query",
        json={
            "query": "foo",
            "filename": "file_doesnt_exist",
        },)
    assert response.status_code == 200
    assert response.json() == {"result": "Cannot find file!"}

def test_valid_file():
    response = client.post("/query",
        json={
            "query": "foo",
            "filename": "home",
        },)
    assert response.status_code == 200
    assert response.json() != {"result": "Cannot find file!"}