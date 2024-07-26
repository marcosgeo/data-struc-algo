
class StarCookie:
    # class atribute
    property = "Star"

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"{self.color}, {self.weight}"


star_cookie1 = StarCookie("red", 16)

print(star_cookie1)
print(star_cookie1.__dict__)
print(StarCookie.__dict__)



class BigTech:
    def __init__(self, username, subscribers=0,  subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1


def show_user(user: BigTech):
    print(f"User {user.username} has subscribers {user.subscribers}")
    print(f"User {user.username} has subscriptions {user.subscriptions}")


user1 = BigTech("Antonio")
user2 = BigTech("Marcos")
user1.subscribe(user2)
show_user(user1)
show_user(user2)

user2.subscribe(user1)
show_user(user2)
show_user(user1)
