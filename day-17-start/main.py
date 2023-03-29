class User:
    def __init__(self, uid, uname):
        self.id = uid
        self.name = uname
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


u1 = User(1, 'sam')
u1.id = 3
u1.name = 'sam j.'
u2 = User(2, 'raj')
print(u1.following, u2.followers)

u1.follow(u2)

print(u1.following, u2.followers)




