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

def test_get_single_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json["name"] == "Wojciech"

def test_get_single_user_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == 404

def test_patch_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    
    response = client.patch('/users/1', json={"name": "Adam"})
    assert response.status_code == 204
    
    response = client.get('/users/1')
    assert response.json["name"] == "Adam"
    assert response.json["lastname"] == "Oczkowski"

def test_patch_user_bad_request(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    
    response = client.patch('/users/1', json={"foo": "bar"})
    assert response.status_code == 400
    
    response = client.patch('/users/999', json={"name": "Test"})
    assert response.status_code == 400

def test_put_user(client):
    response = client.put('/users/5', json={"name": "Put", "lastname": "User"})
    assert response.status_code == 204
    
    response = client.get('/users/5')
    assert response.status_code == 200
    assert response.json["name"] == "Put"

    response = client.put('/users/5', json={"name": "Updated", "lastname": "User"})
    assert response.status_code == 204
    
    response = client.get('/users/5')
    assert response.json["name"] == "Updated"

def test_delete_user(client):
    client.post('/users', json={"name": "Delete", "lastname": "Me"})
    
    response = client.delete('/users/1')
    assert response.status_code == 204
    
    response = client.get('/users/1')
    assert response.status_code == 404

def test_delete_user_not_found(client):
    response = client.delete('/users/999')
    assert response.status_code == 400
