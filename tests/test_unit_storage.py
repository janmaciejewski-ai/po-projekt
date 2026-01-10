import pytest
from app.storage import UserStorage

@pytest.fixture
def storage():
    return UserStorage()

def test_add_user(storage):
    user = storage.add("Jan", "Kowalski")
    assert user["id"] == 1
    assert user["name"] == "Jan"
    assert user["lastname"] == "Kowalski"
    
    users = storage.get_all()
    assert len(users) == 1

def test_get_by_id(storage):
    storage.add("Jan", "Kowalski")
    user = storage.get_by_id(1)
    assert user is not None
    assert user["name"] == "Jan"

    assert storage.get_by_id(999) is None

def test_update_user(storage):
    storage.add("Jan", "Kowalski")
    updated_user = storage.update(1, {"name": "Adam"})
    assert updated_user["name"] == "Adam"
    assert updated_user["lastname"] == "Kowalski"
    
    user = storage.get_by_id(1)
    assert user["name"] == "Adam"

def test_put_user(storage):
    created = storage.put(10, "New", "User")
    assert created is True
    user = storage.get_by_id(10)
    assert user["name"] == "New"

    updated_created = storage.put(10, "Updated", "Name")
    assert updated_created is False
    user = storage.get_by_id(10)
    assert user["name"] == "Updated"

def test_delete_user(storage):
    storage.add("Jan", "Kowalski")
    assert storage.delete(1) is True
    assert len(storage.get_all()) == 0
    assert storage.delete(1) is False
