# Task 1

user = {
    "name": "Alex",
    "age": 31,
    "country": "Poland",
}

for value in user.values():
    print(value)

print()

# Task 2
user["age"] = 32
user["email"] = "alex@example.com"

print(user)

print()

# Task 3

product = {
    "name": "Laptop",
    "price": 1200,
}

if "price" not in product:
    print("No price")

if "discount" not in product:
    print("No discount")


print(product.get("price", "No price"))
print(product.get("discount", "No discount"))

# Task 4

user = {
    "name": "Anna",
    "age": 25,
    "city": "Warsaw",
}

for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(f"{key}: {value}")

print()

# Task 5

settings = {
    "theme": "light",
    "language": "English",
}

settings.update(
    {
        "theme": "dark",
        "notifications": True,
    }
)

print(settings)

print()

# Task 6

user = {
    "name": "Alex",
    "age": 31,
    "password": "secret123",
}

removed_password = user.pop("password")

print(user)
print(removed_password)

print()

# Task 7

user = {
    "name": "Alex",
}

removed_email = user.pop("email", "not found")
print(removed_email)

print()

# Task 8

scores = {
    "Anna": 95,
    "Alex": 67,
    "Maria": 88,
    "John": 54,
    "Kate": 100,
}

for name, score in scores.items():
    if score >= 80:
        print(f"{name}: {score}")

print()

# Task 9

users = [
    {
        "name": "Anna",
        "age": 25,
        "is_active": True,
    },
    {
        "name": "Alex",
        "age": 31,
        "is_active": False,
    },
    {
        "name": "Maria",
        "age": 28,
        "is_active": True,
    },
]

for user in users:
    if user["is_active"]:
        print(user["name"])

print()

# Task 10

user = {
    "name": "Alex",
    "skills": ["Python", "Git", "SQL"],
}

print(user["skills"][1])
user["skills"].append("Docker")

print()

for skill in user["skills"]:
    print(skill)

print()

# Task 11

user = {
    "name": "Anna",
    "address": {
        "country": "Poland",
        "city": "Warsaw",
    },
}

print(user["address"]["city"])
user["address"]["city"] = "Krakow"

print(user["address"])

print()

# Task 12

words = ["cat", "dog", "cat", "bird", "dog", "cat"]

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)

# Task 13

words = ["cat", "dog", "cat", "bird", "dog", "cat"]

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

print()

# Task 14

original = {
    "name": "Alex",
    "skills": ["Python", "Git"],
}

copy_dict = original.copy()

copy_dict["name"] = "John"
copy_dict["skills"].append("SQL")

print(original)
print(copy_dict)

print()

# Task 15

products = [
    {
        "name": "Laptop",
        "price": 1200,
        "in_stock": True,
    },
    {
        "name": "Phone",
        "price": 800,
        "in_stock": False,
    },
    {
        "name": "Monitor",
        "price": 350,
        "in_stock": True,
    },
    {
        "name": "Keyboard",
        "price": 100,
        "in_stock": True,
    },
]

for product in products:
    print(f"{product["name"]}: {product['price']}")

print()

for product in products:
    if product["in_stock"]:
        print(f"{product["name"]}: {product['price']}")

print()

expensive_products = []

for product in products:
    if product["price"] >= 500:
        expensive_products.append(product["name"])

print(expensive_products)

count_products = 0

for product in products:
    count_products += 1

print(f"In stock count: {count_products}")

print()

# Task 16

phone_book = {
    "Anna": "+111111",
    "Alex": "+222222",
    "Maria": "+333333",
}

name = "Alex"

print(phone_book.get(name))

name = "John"

print(phone_book.get(name, "Contact not found"))
