# Task 1


def add(a, b):
    return a + b


assert add(2, 5) == 7
assert add(0, 3) == 3
assert add(-2, 10) == 8
print("Ok.")


# Task 2


def is_adult(age):
    return age >= 18


assert is_adult(17) == False
assert is_adult(18) == True
assert is_adult(25) == True
print("Ok.")

# Task 3


def calculate_total(price, quantity):
    return price * quantity


assert calculate_total(100, 3) == 300
assert calculate_total(50, 0) == 0
assert calculate_total(19.99, 2) == 39.98
print("Ok.")

# Task 4


def is_positive(number):
    return number > 0


assert is_positive(5) == True
assert is_positive(-5) == False
assert is_positive(0) == False

# Task 5


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return age


try:
    validate_age(-25)
except ValueError as error:
    pass
else:
    raise AssertionError("ValueError was not raised")

print("All tests passed")
