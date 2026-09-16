from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    age: int
    is_active: bool = True


user = User("Alex", 31)
print(user)
print(user.name)
print(user.age)

# Task 2

user_1 = User("Anna", 25)
user_2 = User("Alex", 31, False)

print(user_1)
print(user_2)

# Task 3

user_1 = User("Alex", 31)
user_2 = User("Alex", 31)
user_3 = user_1

print(user_1 == user_2)
print(user_1 is user_2)

print(user_1 == user_3)
print(user_1 is user_3)

# Task 4


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def calculate_total(self) -> float:
        return self.price * self.quantity


product = Product("Laptop", 1200.0, 3)

print(product)
print(product.calculate_total())

# Task 5

product.quantity = 5
print(product.calculate_total())

# Task 6


@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)

    def add_member(self, name: str) -> None:
        self.members.append(name)


team_1 = Team("Backend")
team_2 = Team("Frontend")

team_1.members.append("Anna")

print(team_1.members)
print(team_2.members)
print(team_1.members is team_2.members)

# Task 7

team_1.add_member("Alex")
print(team_1)
