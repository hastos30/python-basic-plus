# Task 8
import math

# Task 3
from shop_app import calculations
from shop_app.validation import validate_price, validate_discount, validate_quantity

# Task 4, 5


def main():
    price = 1000
    quantity = 3
    discount = 0.15
    tax = 0.20

    try:
        validate_price(price)
        validate_quantity(quantity)
        validate_discount(discount)
    except ValueError as error:
        print(f"Invalid order: {error}")
    else:
        subtotal = calculations.calculate_subtotal(price, quantity)
        discounted_total = calculations.apply_discount(subtotal, discount)
        final_price = calculations.apply_tax(discounted_total, tax)
        rounded_price = math.ceil(final_price)
        print(f"Subtotal: {subtotal}")
        print(f"After discount: {discounted_total}")
        print(f"Final price: {final_price}")
        print(f"Rounded price: {rounded_price}")


# Task 6

if __name__ == "__main__":
    main()
