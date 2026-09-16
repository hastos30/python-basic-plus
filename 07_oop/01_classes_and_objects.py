# Task 1


class Product:
    pass


product_1 = Product()
product_2 = Product()

print(product_1)
print(isinstance(product_1, Product))
print(product_1 is product_2)

# Task 2


class User:
    pass


user_1 = User()
user_2 = User()

user_3 = user_1

print(user_1 is user_2)
print(user_1 is user_3)

# Task 3


class Order:
    pass


order = Order()

print(isinstance(order, Order))
print(isinstance(order, User))
print(isinstance(order, object))

# Task 4


class Customer:
    pass


class Manager:
    pass


class Payment:
    pass


customer = Customer()
manager = Manager()
payment = Payment()

print(type(customer))
print(type(manager))
print(type(payment))

# class - это шаблон обьекта
# object - это обьект который занимает место в памяти и имеет ссылку
# instance - объект, созданный как  экземпляр определённого класса
