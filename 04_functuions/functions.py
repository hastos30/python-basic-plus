# Task 1


def say_hello():
    print("Hello, Python!")


say_hello()
say_hello()

print()

# Task 2


def greet(name):
    return f"Hello, {name}!"


print(greet("Alex"))
print(greet("Anna"))
print(greet("Maria"))

print()

# Task 3


def calculate_total(price, quantity):
    return price * quantity


print(calculate_total(150, 3))

print()

# Task 4


def create_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(create_greeting("Alex"))
print(create_greeting("Anna", "Hi"))

print()

# Task 5


def create_user(name, age, country="Unknown"):
    return {"name": name, "age": age, "country": country}


print(create_user(age=31, country="Poland", name="Alex"))

print()

# Task 6


def is_adult(age):
    return age >= 18


print()

# Task 7


def check_access(age, is_blocked):
    if age < 18:
        return "Too young"

    if is_blocked:
        return "User blocked"

    return "Access granted"


print(check_access(19, False))
print(check_access(8, False))
print(check_access(25, True))

print()

# Task 8


def get_min_max(numbers):
    return min(numbers), max(numbers)


numbers = [15, 3, 42, 8, 21]

min_number, max_number = get_min_max(numbers)

print(min_number)
print(max_number)

print()

# Task 9


def add_item(items, item):
    new_items = items[:]
    new_items.append(item)
    return new_items


numbers = [1, 2, 3]

new_numbers = add_item(numbers, 4)
print(numbers)
print(new_numbers)

print()

# Task 10


def add_item_in_place(items, item):
    items.append(item)


numbers = [1, 2, 3]
add_item_in_place(numbers, 4)
print(numbers)
# items и numbers ссылаются на один и тот же list,
# а append() мутирует этот объект

print()

# Task 11


def calculate_average(*numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


print(calculate_average(10, 20, 30))
print(calculate_average(5, 10))
print(calculate_average())

print()

# Task 12


def create_profile(name, **details):
    return {"name": name, **details}


profile = create_profile("Alex", age=31, city="Warsaw", language="Python")

print(profile)

print()

# Task 13


def calculate_rectangle(width, height):
    return width * height


size = (10, 5)

print(calculate_rectangle(*size))

rectangle = {
    "width": 8,
    "height": 4,
}

print(calculate_rectangle(**rectangle))

print()

# Task 14

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 50},
    {"name": "Monitor", "price": 350},
    {"name": "Keyboard", "price": 100},
]

products_by_price = sorted(products, key=lambda product: product["price"])

for product in products_by_price:
    print(f"{product["name"]}: {product["price"]}")

print()

# Task 15


def calculate_discount(price, discount):
    """
    Price calculation including the discount

    Args:
        price: Original price.
        discount: Discount as a decimal coefficient, such as 0.2 for 20%.

    Returns:
        Price after applying the discount.
    """
    return price * (1 - discount)


print(calculate_discount(5930, 0.17))

print()

# Task 16

users = [
    {"name": "Anna", "age": 25, "is_active": True},
    {"name": "Alex", "age": 17, "is_active": True},
    {"name": "Maria", "age": 31, "is_active": False},
    {"name": "John", "age": 22, "is_active": True},
    {"name": "Kate", "age": 16, "is_active": False},
]


def get_active_users(users):

    return [user for user in users if user["is_active"]]
    # active_users = []
    # for user in users:
    #     if user["is_active"]:
    #         active_users.append(
    #             {
    #                 "name": user["name"],
    #                 "age": user["age"],
    #                 "is_active": user["is_active"],
    #             }
    #         )
    # return active_users


def get_adult_users(users):

    return [user for user in users if user["age"] >= 18]
    # adult_users = []
    # for user in users:
    #     if user["age"] >= 18:
    #         adult_users.append(
    #             {
    #                 "name": user["name"],
    #                 "age": user["age"],
    #                 "is_active": user["is_active"],
    #             }
    #         )
    # return adult_users


def calculate_average_age(users):
    if not users:
        return None

    users_age = [user["age"] for user in users]
    # users_age = []
    # for user in users:
    #     users_age.append(user["age"])
    return sum(users_age) / len(users_age)


def get_user_names(users):
    return [user["name"] for user in users]
    # users_list = []
    # for user in users:
    #     users_list.append(user["name"])
    # return users_list


users_active = get_active_users(users)
print(users_active)

users_adult = get_adult_users(users_active)
print(users_adult)

users_name = get_user_names(users_adult)
print(users_name)

users_average_age = calculate_average_age(users_adult)
print(users_average_age)

print()

# Task 17

price = 1000
quantity = 3
discount = 0.15
tax = 0.20


def calculate_subtotal(price, quantity):
    """Return the subtotal for the given price and quantity."""
    return price * quantity


def apply_discount(amount, discount):
    """Return the amount after applying a decimal discount."""
    return amount * (1 - discount)


def apply_tax(amount, tax):
    """Return the amount after adding a decimal tax rate."""
    return amount * (1 + tax)


subtotal = calculate_subtotal(price, quantity)
discounted_total = apply_discount(subtotal, discount)
final_price = apply_tax(discounted_total, tax)

print(final_price)
