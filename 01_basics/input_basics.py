# Task 1

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(name, type(name))
print(age, type(age))
print(height, type(height))

print()

# Task 2

age = int(input("Enter your age: "))
print(f"Your age after one year: {age + 1}")

print()

# Task 3

product_name = input("Enter a name product: ")
product_price = float(input("Enter a price product: "))
quantity = int(input("Enter a quantity: "))

total = product_price * quantity

print(f"Total: {total}")

print()

# Task 4

name = input("Enter your name: ")

display_name = name or "Anonymous"

print(display_name)

print()

# Task 5

message = input("Are you a student? yes/no: ")

is_student = "yes" == message

print(is_student)

print()

# Task 6

name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
subscription_answer = input("Do you have subscription? yes/no: ")
has_subscription = subscription_answer == "yes"

can_register = (
    (18 <= age <= 65)
    and (country == "Ukraine" or country == "Poland")
    and has_subscription
)

print(can_register)
