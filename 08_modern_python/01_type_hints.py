# Task 1


def greet(name: str) -> str:
    return f"Hello, {name}"


# Task 2


def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


print(calculate_total(19.99, 3))

# Task 3


def print_user(name: str) -> None:
    print(f"User: {name}")


# Task 4

users = [
    {"name": "Anna", "age": 25},
    {"name": "Alex", "age": 17},
    {"name": "Maria", "age": 31},
]


def get_adult_names(users: list[dict[str, int]]) -> list[str]:
    return [user["name"] for user in users if user["age"] >= 18]


print(get_adult_names(users))

# Task 5


def find_user(users: list[dict[str, str]], name: str) -> str | None:
    for user in users:
        if user["name"] in name:
            return user["name"]

    return None


print(find_user(users, "Anna"))
print(find_user(users, "John"))

# Task 6


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self) -> float:
        return self.price * self.quantity


product = Product("Laptop", 1200.0, 2)
print(product.calculate_total())

# Task 7


def set_age(age: int) -> int:
    if age < 0:
        raise ValueError("Age cannot be negative")

    return age


print(set_age(31))
try:
    print(set_age(-5))
except ValueError as error:
    print(error)


# Task 8


def greet(name: str) -> str:
    return f"Hello, {name}"


print(greet(123))
