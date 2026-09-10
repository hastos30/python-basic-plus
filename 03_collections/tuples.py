# Task 1

point = (10, 20, 30)

print(point[0])
print(point[-1])
print(len(point))

print()

# Task 2

numbers = (10, 20, 30, 40, 50)

my_first_slice = numbers[1:4]
my_second_slice = numbers[::-1]

print(my_first_slice)
print(my_second_slice)

print()

# Task 3

single = ("Python",)
print(type(single))

print()

# Task 4

values = (10, 20, 10, 30, 10)

print(values.count(10))
print(values.index(30))

print()

# Task 5

user = ("Alex", 31, "Poland")

name, age, country = user

print(f"{name} is {age} years old and lives in {country}")

print()

# Task 6

numbers = (10, 20, 30, 40, 50)

# *middle - list type
first, *middle, last = numbers

print(first, middle, last)

print()

# Task 7

a = 10
b = 20

print(a, b)

a, b = b, a

print(a, b)

print()

# Task 8

languages = ("Python", "Go", "Rust")

for language in languages:
    print(language)

print()

# Task 9

data = (
    [1, 2],
    [3, 4],
)

data[0].append(5)

print(data)

print()

# Task 10

# list - поскольку список дел - может мутироваться (добавляться, отменяться, изменяться)
tasks = ["Проснуться", "Пойти на работу", "Купить продукты", "Лечь спать до 22:00"]

# tuple - поскольку это стандарт, который не будет изменятся.
screen_resolution = (1920, 1080)

# Task 11

users = (
    ("Anna", 25),
    ("Alex", 31),
    ("Maria", 28),
)

for user in users:
    name, age = user
    if age > 27:
        print(f"{name}: {age}")

for name, age in users:
    if age > 27:
        print(f"{name}: {age}")
