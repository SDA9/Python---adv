class User:
    def __init__(self, user_id, username, password, points):
        self.id = user_id
        self.username = username
        self.password = password
        self.points = 0
        

user_1 = User("001", "adams", "kerjsejri")



print(user_1.username)

#user_2 = User()
#user_2.id = "002"
#user_2.username = "anony"
