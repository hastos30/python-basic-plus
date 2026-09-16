# Task


class Product:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price


product_1 = Product("Laptop", 1200)
product_2 = Product("Mouse", 50)

print(product_1.category)
print(product_2.category)
print(Product.category)

# Task 2

Product.category = "Tech"
print(product_1.category)
print(product_2.category)
print(Product.category)

# Task 3

product_1.category = "Computers"
print(product_1.category)
print(product_2.category)
print(Product.category)
# потому что сперва атрибут ищет в экземпляре класса, а если его не находит - ищет в атрибуте класса. Потому product_1 - определил свою версию атрибута

# Task 4


class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1


user_1 = User("Anna")
user_2 = User("Alex")
user_3 = User("Maria")

print(User.count)

# Task 5


class Team:
    # members = []
    def __init__(self):
        self.members = []


team_1 = Team()
team_2 = Team()

team_1.members.append("Anna")

print(team_1.members)
# print(team_2.members)
# print(Team.members)


# Task 6

print(team_1.members is team_2.members)
