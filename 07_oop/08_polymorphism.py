class Employee:

    def work(self):
        return "Employee is working"


class Developer(Employee):
    def work(self):
        return "Developer is writing code"


class Manager(Employee):
    def work(self):
        return "Manager is managing the team"


employee = Employee()
developer = Developer()
manager = Manager()

print(employee.work())
print(developer.work())
print(manager.work())


# Task 2

employees = [
    employee,
    developer,
    manager,
]

for employee in employees:
    print(employee.work())

# Task 3


def start_work(employee):
    return employee.work()


print(start_work(employee))
print(start_work(developer))
print(start_work(manager))

# Task 4


class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Task 5


def make_sound(animal):
    return animal.speak()


print(make_sound(Dog()))
print(make_sound(Cat()))

# Task 6


class Fish:
    pass


fish = Fish()

try:
    print(make_sound(fish))
except AttributeError as error:
    print(error)

# Polymorphism - это один интерфейс - много реалзиаций
# duck typing - если бегает как утка, выглядит как утка - это утка
