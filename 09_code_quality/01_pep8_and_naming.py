# Task 1

price = 1000
quantity = 3
total_price = price * quantity

print(total_price)

print()

# Task 2

user_name = "Alex"
user_age = 31
is_active = True

print()

# Task 3

numbers = [10, 20, 30]

sum_numbers = 0

for number in numbers:
    sum_numbers += number

print(sum_numbers)

print()

# Task 4

MAX_ATTEMPTS = 5
attempts = 0

if attempts >= MAX_ATTEMPTS:
    print("Too many attempts")


print()

# Task 5

users = [
    {
        "name": "Anna",
        "age": 25,
    },
    {
        "name": "Alex",
        "age": 31,
    },
    {
        "name": "Maria",
        "age": 22,
    },
]

oldest = max(users, key=lambda user: user["age"])
print(oldest)

print()

# Task 6

is_active = True
has_access = False
can_edit = True

print()

# Task 7

# snake_case используется для названия переменных и функций
# PascalCase используется для классов
# UPPER_CASE используется для констант, которые на самом деле являются обычными переменными, но по соглашению программисты значение не изменяют
