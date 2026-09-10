# Task 1

numbers = [1, 2, 3, 4, 5]

squares = [number**2 for number in numbers]
print(squares)

print()

# Task 2

my_number = [number for number in range(1, 21) if number % 3 == 0]
print(my_number)

print()

# Task 3

numbers = [1, 2, 3, 4, 5, 6]

squares_even_number = [number**2 for number in numbers if number % 2 == 0]

print(squares_even_number)

print()

# Task 4

names = ["   alex ", "ANNA", " maria", "JOHN   "]

clean_names = [name.strip().title() for name in names]

print(clean_names)

print()

# Task 5

numbers = [1, 2, 3, 4, 5, 6]

my_list = ["odd" if number % 2 != 0 else "even" for number in numbers]

print(my_list)

print()

# Task 6

languages = ["Python", "python", "Go", "GO", "Java", "java", "Python"]

languages_set = {language.lower() for language in languages}
print(languages_set)

print()

# Task 7

squares = {value: value**2 for value in range(1, 6)}
print(squares)

print()

# Task 8

scores = {
    "Anna": 95,
    "Alex": 67,
    "Maria": 88,
    "John": 54,
    "Kate": 100,
}

passed_scores = {name: score for name, score in scores.items() if score >= 70}

print(passed_scores)

print()

# Task 9

statuses = {
    name: "passed" if score >= 70 else "failed" for name, score in scores.items()
}
print(statuses)

print()

# Task 10

users = [
    {"name": "Anna", "age": 25, "is_active": True},
    {"name": "Alex", "age": 31, "is_active": False},
    {"name": "Maria", "age": 28, "is_active": True},
    {"name": "John", "age": 19, "is_active": True},
]

active_adults = [
    user["name"] for user in users if user["is_active"] and user["age"] >= 21
]
print(active_adults)

print()

# Task 11

ages_by_name = {user["name"]: user["age"] for user in users}
print(ages_by_name)

print()

# Task 12

pairs = [(row, column) for row in range(1, 4) for column in range(1, 4)]
print(pairs)

# Task 13

names = ["Anna", "Alex", "Maria"]

for name in names:
    print(name)

# потому что нам нужно просто перебрать значения в list - а comprehension сохраняет данные в новой переменной

print()

# Task 14

products = [
    {"name": "Laptop", "price": 1200, "in_stock": True},
    {"name": "Phone", "price": 800, "in_stock": False},
    {"name": "Monitor", "price": 350, "in_stock": True},
    {"name": "Keyboard", "price": 100, "in_stock": True},
    {"name": "Tablet", "price": 600, "in_stock": True},
]

product_names = [product["name"] for product in products]
print(product_names)

available_products = [product["name"] for product in products if product["in_stock"]]
print(available_products)

expensive_products = [
    product["name"] for product in products if product["price"] >= 500
]
print(expensive_products)

prices = {product["name"]: product["price"] for product in products}
print(prices)

print()

# Task 15

words = ["cat", "developer", "python", "go", "programming", "linux"]

my_list = [word.upper() for word in words if len(word) > 5]
print(my_list)
