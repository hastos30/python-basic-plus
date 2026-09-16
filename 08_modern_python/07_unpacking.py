# Task 1

user = ("Alex", 31)
name, age = user

print(name, age)

# Task 2

numbers = [10, 20, 30, 40, 50]
first, *rest = numbers
print(first, rest)

# Task 3

first, *middle, last = numbers
print(first, middle, last)

# Task 4

a = 10
b = 20
print(a, b)

a, b = b, a
print(a, b)

# Task 5


def multiply(a, b, c):
    return a * b * c


numbers = [2, 3, 4]

print(multiply(*numbers))

# Task 6


def create_user(name, age, city):
    return f"{name}, {age}, {city}"


user_data = {
    "name": "Anna",
    "age": 25,
    "city": "Kyiv",
}

print(create_user(**user_data))
