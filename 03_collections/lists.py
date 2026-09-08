# Task 1

languages = ["Python", "Java", "C++", "JavaScript"]
print(languages[0])
print(languages[-1])
languages[1] = "Go"
print(languages)

print()

# Task 2

numbers = [10, 20, 30, 40, 50, 60, 70]

first_thre = numbers[:3]
print(first_thre)
last_there = numbers[4:]
print(last_there)
middle = numbers[2:5]
print(middle)
reversed_number = numbers[:]
reversed_number.reverse()
print(reversed_number)
every_second = numbers[::2]
print(every_second)

print()

# Task 3

users = ["Anna", "Alex"]

users.insert(1, "Maria")
users.insert(len(users) - 1, "Viktor")
users.append("John")
users.extend(["Kate"])

print(users)

print()

# Task 4

first = [1, 2]
second = [1, 2]

first.append([3, 4])
print(first)
second.extend([3, 4])
print(second)

print()

# Task 5

animals = ["cat", "dog", "parrot", "dog", "hamster"]

animals.remove("dog")
removed_animal = animals.pop()
print(animals)
print(removed_animal)

print()

# Task 6

numbers = [10, 20, 10, 30, 40, 10, 50]

print(numbers.index(30))
print(numbers.count(10))
print(100 in numbers)

print()

# Task 7

scores = [78, 95, 61, 88, 100, 73]

print(f"origina: {scores}")
print(f"ascending: {sorted(scores)}")
print(f"descending: {sorted(scores, reverse=True)}")

print()

# Task 8

even_numbers = []

for number in range(1, 21):
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

even_numbers = [number for number in range(1, 21) if number % 2 == 0]
print(even_numbers)

print()

# Task 9

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number**2)

print(squares)

squares = [number**2 for number in numbers]
print(squares)

print()

# Task 10

words = ["python", "hi", "developer", "cat", "programming", "go"]

long_words = []

for word in words:
    if len(word) > 5:
        long_words.append(word)

print(long_words)

long_words = [word for word in words if len(word) > 5]
print(long_words)

print()

# Task 11

users = [
    ["Anna", 25],
    ["Alex", 31],
    ["Maria", 28],
]

for name, age in users:
    print(f"{name} is {age} years old")

print()

# Task 12

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])

print()

for i in matrix:
    for j in i:
        print(j)

print()

# Task 13

prices = [120, 80, 250, 50, 100]

print(f"Minimum: {min(prices)}")
print(f"Maximum: {max(prices)}")
print(f"Total: {sum(prices)}")
print(f"Average: {sum(prices) / len(prices)}")

print()

# Task 14

a = [1, 2, 3]
b = a

b[0] = 100

print(a)
print(b)

a = [1, 2, 3]
b = a[:]

b[0] = 100

print(a)
print(b)

print()

# Task 15

original = [
    [1, 2],
    [3, 4],
]

copy_list = original[:]

copy_list[0][0] = 999
print(original)
print(copy_list)

print()

# Task 16

scores = [78, 95, 61, 88, 100, 73, 95, 54]

print(f"Count: {len(scores)}")
print(f"Minimum: {min(scores)}")
print(f"Maximum: {max(scores)}")
print(f"Averge: {sum(scores) / len(scores)}")

passed_scores = [number for number in scores if 70 <= number < 90]
excellent_scores = [number for number in scores if number >= 90]
print(f"Passed: {passed_scores}")
print(f"Excellent: {excellent_scores}")
print(f"95 count: {scores.count(95)}")

sorted_scores = sorted(scores)
print(f"Sorted: {sorted_scores}")
print(f"Original: {scores}")

print()

# Task 17

queue = []

queue.append("Anna")
queue.append("Alex")
queue.append("Maria")

for name in queue:
    print(name)

current_user = queue.pop(0)
print(f"Serving: {current_user}")
print(queue)
