# Task 1

numbers = [5, 2, 9, 1, 7]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print(numbers)
print(ascending)
print(descending)

# Task 2

names = ["Maria", "Alex", "Anna", "John"]

names_sorted = sorted(names)
print(names_sorted)

# Task 3

users = [
    {"name": "Anna", "age": 25},
    {"name": "Alex", "age": 31},
    {"name": "Maria", "age": 22},
]

users_sorted_age = sorted(users, key=lambda user: user["age"])
print(users_sorted_age)

# Task 4

users_sorted_age_old_to_jung = sorted(users, key=lambda user: user["age"], reverse=True)
print(users_sorted_age_old_to_jung)

# Task 5

users_sorted_name = sorted(users, key=lambda user: user["name"])
print(users_sorted_name)
