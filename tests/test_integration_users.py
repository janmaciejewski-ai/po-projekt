import pytest
from app.app import app
from app.storage import storage

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        storage.clear()
        yield client

def test_get_users_empty(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json == []

def test_create_user(client):
    response = client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    assert response.status_code == 201
    assert response.json["name"] == "Wojciech"
    assert "id" in response.json
