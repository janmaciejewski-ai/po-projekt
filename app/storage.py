class UserStorage:
    def __init__(self):
        self._users = {}
        self._next_id = 1

    def get_all(self):
        return list(self._users.values())

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

storage = UserStorage()
