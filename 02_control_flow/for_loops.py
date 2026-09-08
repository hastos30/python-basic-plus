# Task 1

language = "Python"

for text in language:
    print(text)

print()

# Task 2

for number in range(1, 11):
    print(number)

print()

# Task 3

for number in range(2, 11, 2):
    print(number)

print()

# Task 4

for number in range(10, 0, -1):
    print(number)
print("Go!")

print()

# Task 5

for _ in range(1, 6):
    print("Hello")

print()

# Task 6

for number in range(1, 21):
    if number % 3 == 0:
        print(number)

print()

# Task 7

for number in range(1, 11):
    if number % 3 == 0:
        continue
    print(number)

print()

# Task 8

for number in range(1, 100):
    print(number)
    if number == 7:
        break


# Task 9

word = "Python"

for index in range(len(word)):
    print(index, word[index])

print()

# Task 10

for row in range(1, 4):
    for column in range(1, 4):
        print(row, column)

print()

# Task 11

for row in range(1, 11):
    for column in range(1, 11):
        print(f"{row} * {column} = {row * column}", end="\t")

    print()

print()

# Task 12

for row in range(1, 4):
    for column in range(1, 6):
        if column > 3:
            break
        print(row, column)

print()

# Task 13

for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Task 14

for low in range(1, 7):
    for column in range(1, low):
        print("*", end="")

    print()
