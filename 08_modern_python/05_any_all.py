# Task 1

values = [False, False, True, False]

print(any(values))
print(all(values))

# Task 2

numbers = [2, 4, 6, 8]

print(all(number % 2 == 0 for number in numbers))

# Task 3

numbers = [2, 4, 7, 8]

print(any(number % 2 != 0 for number in numbers))

print()

# Task 4

users = [
    {"name": "Anna", "is_active": True},
    {"name": "Alex", "is_active": False},
    {"name": "Maria", "is_active": True},
]

print(any(user["is_active"] for user in users))
print(all(user["is_active"] for user in users))

# Task 5

passwords = ["secret123", "qwerty", "python2026"]

print(all(len(password) >= 6 for password in passwords))
