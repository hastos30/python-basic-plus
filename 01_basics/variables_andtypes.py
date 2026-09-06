# Task 1

user_name = "Viktor"
user_age = 31
user_height = 1.87
is_student = False
is_married = None

print(user_name, type(user_name))
print(user_age, type(user_age))
print(user_height, type(user_height))
print(is_student, type(is_student))
print(is_married, type(is_married))

print()
# Task 2

value = 10
print(value, type(value))
value = 10.9
print(value, type(value))
value = "20"
print(value, type(value))
value = True
print(value, type(value))
value = None
print(value, type(value))

print()
# Task 3

age = "25"
height = "1.82"
score = 95
empty_value = ""

age = int(age)
print(age, type(age))
height = float(height)
print(height, type(height))
score = str(score)
print(score, type(score))
empty_value = bool(empty_value)
print(empty_value, type(empty_value))

print()

# Task 4

value_1 = 0
value_2 = 10
value_3 = ""
value_4 = "False"
value_5 = None

print(bool(value_1))  # False
print(bool(value_2))  # True
print(bool(value_3))  # False
print(bool(value_4))  # True
print(bool(value_5))  # False

print()

# Task 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True
print(a is b)  # False

print(a == c)  # True
print(a is c)  # True

print()

# Task 6

product_name = "Monitor"
product_price = 10000
quantity = 3
is_in_stock = True
discount = None

print(product_name, type(product_name))
print(product_price, type(product_price))
print(quantity, type(quantity))
print(is_in_stock, type(is_in_stock))
print(discount, type(discount))

product_price = str(product_price)
quantity = float(quantity)
print(product_price, type(product_price))
print(quantity, type(quantity))
print(discount is None)
