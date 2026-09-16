# Task 1

names = ["Anna", "Alex", "Maria"]
ages = [25, 31, 28]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Task 2

products = ["Laptop", "Mouse", "Keyboard"]
prices = [1200, 50, 100]

my_product = dict(zip(products, prices))

print(my_product)

# Task 3

quantities = [2, 5, 3]

for name, price, quantity in zip(products, prices, quantities):
    print(f"{name}: {price} x {quantity} = {price*quantity}")

# Task 4

letters = ["A", "B", "C", "D"]
numbers = [1, 2]

result = list(zip(letters, numbers))
print(result)
