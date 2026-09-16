# Task 1


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name} earns {self.salary}"


# Task 2


class Manager(Employee):
    def hold_meeting(self):
        return f"{self.name} is holding a meeting"


manager = Manager("Anna", 3000)
print(manager.name)
print(manager.salary)
print(manager.get_info())


# Task 3


class Developer(Employee):
    def write_code(self):
        return f"{self.name} is writing code"


developer = Developer("Alex", 2500)

print(developer.get_info())

# Task 4

print(isinstance(manager, Manager))
print(isinstance(manager, Employee))
print(isinstance(manager, object))

print(isinstance(developer, Manager))
print(isinstance(developer, Employee))
print(isinstance(developer, object))

# Task 5

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Employee, Manager))

# Task 6 ^

print(manager.hold_meeting())
print(developer.write_code())
