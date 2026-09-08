# Task 1

age = int(input("Enter your age: "))

if age < 0:
    print("Ivalid age")
elif age < 18:
    print("Minor")
elif 18 <= age <= 65:
    print("Adult")
else:
    print("Senior")

# Task 2

score = 87

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 50:
    print("Passed")
else:
    print("Failde")

# Task 3

age = 25
has_ticket = True
is_blocked = False

if age >= 18 and has_ticket and not is_blocked:
    print("Acces granted")
else:
    print("Access denied")

# Task 4

operation = input("Continue? yes/no").strip().lower()

if operation == "yes":
    print("Continue")
elif operation == "no":
    print("Stop")
else:
    print("Ivalid answer")

# Task 5

is_logged_in = True
is_admin = False

if not is_logged_in:
    print("Please log in")
else:
    if is_admin:
        print("Admin panel")
    else:
        print("User dashboard")

# Task 6

age = 25
has_subscription = True

if age >= 18:
    print("Adult user")

if has_subscription:
    print("Subscriber")

# Task 7

user_age = int(input("Enter your age: "))
user_country = input("Enter your country: ")
is_subscription = input("Do you have subscription? yes/no: ").strip().lower()
is_blocked = input("Do you blocked? yes/no: ").strip().lower()

if user_age < 0:
    print("Invalid age")
elif user_age < 18:
    print("Too young")
elif user_country != "Ukraine" and user_country != "Poland":
    print("Country not supported")
elif is_subscription != "yes":
    print("Subscription required")
elif is_blocked == "yes":
    print("User blocked")
else:
    print("registration allowed")
