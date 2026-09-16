class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User {self.name}, {self.age} years old"

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r})"


user = User("Alex", 31)

print(user)

# Task 2

print(repr(user))

# Task 3

users = [
    User("Anna", 25),
    User("Alex", 31),
]

print(users)

for user in users:
    print(user)

# Task 4


class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

    def add_member(self, name):
        self.members.append(name)

    def __str__(self):
        return f"Team with {self.__len__()} members"


team = Team(["Anna", "Alex", "Maria"])
print(len(team))

# Task 5

team.add_member("John")
print(len(team))

# Task 6

print(team)
