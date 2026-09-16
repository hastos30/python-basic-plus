# Task 1

names = ["Anna", "Alex", "Maria"]

for index, name in enumerate(names):
    print(f"{index} {name}")

# Task 2

for index, name in enumerate(names, start=1):
    print(index, name)

# Task 3

tasks = ["Code", "Test", "Deploy"]
for task, value in enumerate(tasks, start=1):
    print(f"Task {task}: {value}")

# Task 4

numbers = [10, 20, 30, 40]
for index, number in enumerate(numbers):
    if number > 20:
        print(f"Index {index}: {number}")
