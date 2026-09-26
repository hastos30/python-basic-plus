# Task 1

price = 1000
quantity = 3
discount = 0.15
tax = 0.20

subtotal = price * quantity
discounted_total = subtotal * (1 - discount)
final_total = discounted_total * (1 + tax)

# Task 2


def get_status(age):
    if age < 18:
        return "minor"
    return "adult"


# Task 3


def is_positive(number):
    return number > 0


# Task 4


def get_access(age, is_active):
    if age >= 18:
        if is_active:
            return "Acces granted"
        return "Account inactive"
    return "Too young"


# Task 5


def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(1000, 3)
print(f"Total: {total}")


# Task 6


def calculate_total(price, quantity):
    return price * quantity


laptop_total = calculate_total(1200, 2)
mouse_total = calculate_total(50, 5)
keyboard_total = calculate_total(100, 3)
