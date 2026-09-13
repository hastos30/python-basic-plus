# Task 1
def calculate_subtotal(price, quantity):
    return price * quantity


def apply_discount(amount, discount):
    return amount * (1 - discount)


def apply_tax(amount, tax):
    return amount * (1 + tax)


# Task 7

if __name__ == "__main__":
    print(calculate_subtotal(100, 2))
