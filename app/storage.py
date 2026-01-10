class UserStorage:
    def __init__(self):
        self._users = {}
        self._next_id = 1

    def get_all(self):
        return list(self._users.values())

    def get_by_id(self, user_id):
        return self._users.get(user_id)

    def add(self, name, lastname):
        user_id = self._next_id
        self._next_id += 1
        user = {
            "id": user_id,
            "name": name,
            "lastname": lastname
        }
        self._users[user_id] = user
        return user

    def update(self, user_id, data):
        if user_id in self._users:
            self._users[user_id].update(data)
            return self._users[user_id]
        return None
    
    def put(self, user_id, name, lastname):
        if user_id in self._users:
            self._users[user_id] = {"id": user_id, "name": name, "lastname": lastname}
            return False
        else:
            self._users[user_id] = {"id": user_id, "name": name, "lastname": lastname}
            if user_id >= self._next_id:
                self._next_id = user_id + 1
            return True

    def delete(self, user_id):
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False
    
    def clear(self):
        self._users = {}
        self._next_id = 1

storage = UserStorage()
