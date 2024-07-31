class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user1 = User("001", "avisheet")
print(user1.username)

