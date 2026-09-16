# Task 1

numbers = [10, 25, 5, 40, 20]
print(sum(numbers))
print(min(numbers))
print(max(numbers))

# Task 2

prices = [19.99, 5.50, 100.0, 42.75]

print(sum(prices))

for price in prices:
    print(round(price, 2))

# Task 3

temperature = -12
print(abs(temperature))

# Task 4

users = [
    {"name": "Anna", "age": 25},
    {"name": "Alex", "age": 31},
    {"name": "Maria", "age": 22},
]

print(min(users, key=lambda user: user["age"]))
print(max(users, key=lambda user: user["age"]))

# Task 5

actual = 97
expected = 100

diff = abs(expected - actual)
print(diff)

# Task 6

numbers = [2.345, 7.891, 10.555]

new_numbers = [round(number, 2) for number in numbers]
print(new_numbers)
