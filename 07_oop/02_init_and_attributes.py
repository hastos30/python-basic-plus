# Task 1


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


product_1 = Product("Laptop", 1200, 2)
product_2 = Product("Mouse", 50, 5)

print(product_1.name)
print(product_1.price)
print(product_1.quantity)

print(product_2.name)
print(product_2.price)
print(product_2.quantity)

# Task 2

product_1.quantity = 3

print(product_1.quantity)
print(product_2.quantity)

# Task 3


class User:
    def __init__(self, name, age, is_active=True):
        self.name = name
        self.age = age
        self.is_active = is_active


user_1 = User("Anna", 25)
user_2 = User("Alex", 31, False)

print(user_1.name)
print(user_1.age)
print(user_1.is_active)

print(user_2.name)
print(user_2.age)
print(user_2.is_active)

# Task 4


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


account_1 = BankAccount("Anna", 1000)
account_2 = BankAccount("Alex", 500)

account_1.balance += 250
account_2.balance -= 100

print(account_1.owner, account_1.balance)
print(account_2.owner, account_2.balance)

# Task 5

account_3 = account_1

account_3.balance += 500

print(account_1.balance)
print(account_3.balance)
print(account_1 is account_3)

# Потому что переменная получила ссылку на которую ссылается уже переменная... и получилось что две переменные ссылаются на один и тот же самый обьект
