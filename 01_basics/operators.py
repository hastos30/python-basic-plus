# Task 1

a = 17
b = 5

print(a + b, type(a + b))
print(a - b, type(a - b))
print(a * b, type(a * b))
print(a // b, type(a // b))
print(a / b, type(a / b))
print(a % b, type(a % b))
print(a**b, type(a**b))

print()

# Task 2

result = (2 + 3) + 4 + 10 - 5  # 14
result = (3 + 4 + 10 + 5) - 2  # 20
result = (2 * 3 - 4) * (10 - 5)  # 10

print()

# Task 3

score = 100

score += 50
print(score, type(score))
score *= 2
print(score, type(score))
score -= 75
print(score, type(score))
score /= 5
print(score, type(score))

print()

# Task 4

age = 31
minimum_age = 18
maximum_age = 65

is_adult = age >= minimum_age
print(is_adult)
is_too_old = age > maximum_age
print(is_too_old)
is_working_age = minimum_age <= age <= maximum_age
print(is_working_age)

print()

# Task 5

age = 25
has_ticket = True
is_blocked = False

can_enter = age >= 18 and has_ticket and not is_blocked

# Task 6

is_admin = False
is_manager = True

has_access = is_admin or is_manager

# Task 7

enter_name = ""

display_name = enter_name or "Anonymous"
print(display_name)

# Task 8

language = "Python"

print("Py" in language)
print("Java" not in language)


# Task 9

user_age = 22
user_country = "Ukraine"
has_subscription = True
is_blocked = False

can_use_service = (
    (user_age >= 18 and user_age <= 65)
    and (user_country == "Ukraine" or user_country == "Poland")
    and has_subscription
    and not is_blocked
)
