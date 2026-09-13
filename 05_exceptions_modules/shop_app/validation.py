# Task 2


def validate_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative")
    return price


def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    return quantity


def validate_discount(discount):
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0 and 1")
    return discount
