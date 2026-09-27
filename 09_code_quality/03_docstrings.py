# Task 1


def calculate_total(price: float, quantity: int) -> float:
    """calculate subtotal price"""
    return price * quantity


# Task 2


def is_adult(age: int) -> bool:
    """person is of legal age or not"""
    return age >= 18


is_adult()

# Task 3


def divide(a: float, b: float) -> float:
    """division one number by another

    Args:
        a (float): dividend
        b (float): divisor

    Raises:
        ValueError: if b is zero

    Returns:
        float: result division a by b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
