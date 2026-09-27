# Task 1


# Complexity O(1)
def get_first(items):
    return items[0]


# Task 2


# Complexity O(n)
def calculate_sum(numbers):
    result = 0
    for number in numbers:
        result += number

    return result


# Task 3


# Complexity O(n)
def contains(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False


# Task 4

# Complexity O(n**2)


def get_pairs(numbers):
    return [(i, j) for i in numbers for j in numbers]


print(get_pairs([1, 2]))

# Task 5

# A O(1)
value = numbers[0]

# B O(n)
for number in numbers:
    print(number)

# C O(n)
for number in numbers:
    print(number)

for number in numbers:
    print(number)

# D O(n**2)
for first in numbers:
    for second in numbers:
        print(first, second)
