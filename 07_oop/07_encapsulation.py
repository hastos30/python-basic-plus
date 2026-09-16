# Task 1


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Indufficient funds")

        self._balance -= amount


account = BankAccount("Anna", 1000)

print(account.owner)
print(account.get_balance())

# Task 2

account.deposit(500)
print(account.get_balance())

# Task 3

account.withdraw(200)
print(account.get_balance())

# Task 4

# Проверка была

# Task 5

# print(account._balance)
# account._balance = -100000
# print(account.get_balance())

# Task 6


class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password


user = User("Alex", "secret123")
print(user.name)
print(user.__password)
print(user._User__password)
