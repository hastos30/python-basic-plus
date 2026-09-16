# Task 1


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "Employee is working"

    def get_info(self):
        return f"{self.name} earns {self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        return "Developer is writing code"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, language: {self.programming_language}"


# employee = Employee()
developer = Developer("Alex", 3000, "Python")

# print(employee.work())
print(developer.work())

# Task 2

print(developer.name)
print(developer.salary)
print(developer.programming_language)

# Task 3

print(developer.get_info())

# Task 4


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return "Manager is managing the team"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, team size: {self.team_size}"


manager = Manager("Anna", 4000, 8)

print(manager.get_info())

# Task 5

print(manager.work())

# Task 6

developer = Developer("Alex", 3000, "Python")
manager = Manager("Anna", 4000, 8)

print(developer.get_info())
print(developer.work())

print(manager.get_info())
print(manager.work())

print(isinstance(developer, Employee))
print(isinstance(manager, Employee))
