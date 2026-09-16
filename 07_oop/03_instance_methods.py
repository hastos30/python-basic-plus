# Task 1


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def add_stock(self, amount):
        self.quantity += amount


product = Product("Laptop", 1200, 3)

print(product.calculate_total())

# Task 2

product.add_stock(2)
print(product.calculate_total())

# Task 3


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("Anna", 1000)

account.deposit(500)
account.withdraw(200)

print(account.get_balance())

# Task 4

account_1 = BankAccount("Anna", 1000)
account_2 = BankAccount("Alex", 500)

account_1.deposit(300)
account_2.withdraw(100)

print(account_1.get_balance())
print(account_2.get_balance())
