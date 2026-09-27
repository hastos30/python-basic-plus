# Task 1


def calc(p, q, d):
    x = p * q
    y = x * (1 - d)
    return y


def calculate_total_price(price, quantity, discount):
    sum_price = price * quantity
    total_price = sum_price * (1 - discount)
    return total_price


# Task 2


def get_status(age, is_active):
    if age >= 18:
        if is_active:
            return "active adult"
        else:
            return "inactive adult"
    else:
        return "minor"


def get_status(age, is_active):
    if age < 18:
        return "minor"

    if is_active:
        return "active adult"

    return "inactive adult"


# Task 3


def get_laptop_total():
    return 1200 * 2


def get_mouse_total():
    return 50 * 5


def get_keyboard_total():
    return 100 * 3


def calculate(price, quantity):
    return price * quantity


# Task 4


def process_user(name, age):
    if age < 0:
        raise ValueError("Invalid age")

    return f"{name}: adult" if age >= 18 else f"{name}: minor"


print(process_user("Viktor", 31))

# Task 5

assert calculate_total_price(1000, 3, 0.15) == 2550
print("Ok.")
