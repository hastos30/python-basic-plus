# Task 1

text = "123"
try:
    text_int = int(text)
except ValueError:
    print("Invalid number")


# Task 2


def divide(a, b):
    return a / b


try:
    divide(10, 2)
except ZeroDivisionError:
    print("Cannot division be zero")
except TypeError:
    print("Incompatible data type")

# Task 3

user = {
    "name": "Alex",
}

try:
    user["age"]
except KeyError:
    print("Age not found")

# Task 4

text = "25"

try:
    text_int = int(text)
except ValueError:
    print("Number is not correct")
else:
    print(text_int**2)

# Task 5

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age")
else:
    print(f"Age: {age}")
finally:
    print("Parsing finished")

# Task 6

try:
    int("Hello")
except ValueError as error:
    print(f"Conversion failed: {error}")

# Task 7

while True:
    try:
        number = int(input("Enter a integer: "))
        break
    except ValueError:
        print("Invalid integer, try again")

# Task 8


def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age > 130:
        raise ValueError("Age is unrealistic")

    return age


try:
    set_age(250)
except ValueError as error:
    print(error)

# Task 9


def calculate_discount(price, discount):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0 and 1")

    return price * (1 - discount)


try:
    calculate_discount(-100, 0.2)
except ValueError as error:
    print(error)


# Task 10


def parse_number(text):
    try:
        return int(text)
    except ValueError:
        print(f"Failed to parse: {text}")
        raise


# Task 11


def parser_age(text):
    try:
        age = int(text)
    except ValueError:
        print("Invalid type")
        return None
    else:
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age


try:
    parser_age("-5")
except ValueError as error:
    print(error)

# Task 12


def calculate(a, b, operation):
    if not operation in ("+", "-", "*", "/"):
        raise ValueError("Unsupported operation")
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b

    return a / b


try:
    print(calculate("10", 5, "-"))
except ValueError as error:
    print(error)
except ZeroDivisionError:
    print("Cannot divition be zero")
except TypeError:
    print("Invalid type")
