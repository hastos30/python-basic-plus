# Task 1

count = 1

while count <= 5:
    print(count)
    count += 1

print()

# Task 2

count = 5

while count > 0:
    print(count)
    count -= 1
print("Go!")

print()

# Task 3

count = 1

while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1

print()

# Task 4

count = 0

while count < 5:
    count += 1
    if count == 3:
        continue

    print(count)

print()

# Task 5

count = 0

while count < 10:
    if count == 5:
        break

    count += 1

    print(count)

print("Loop finished")

print()

# Task 6

answer = ""

while True:
    answer = input("Enter yes/no: ").strip().lower()
    if answer == "yes" or answer == "no":
        break

    print("Invalid answer")

print()

# Task 7

while True:
    name = input("Enter your name: ").strip()
    if name.isalpha():
        print(f"Hello, {name.title()}")
        break

print()

# Task 8

correct_password = "python123"
max_attempts = 3
attempts_left = 0

while True:
    input_password = input("Enter password: ")

    if input_password == correct_password:
        print("Access granted")
        break

    print("Wrong password")
    attempts += 1
    print(f"Attempts left: {max_attempts - attempts_left}")

    if attempts == max_attempts:
        print("Acces denied")
        break

# Task 9

while True:
    command = input("Command: ").strip().lower()

    if command not in ("start", "status", "help", "exit"):
        print("Unknown command")
    else:
        if command == "start":
            print("Program started")

        elif command == "status":
            print("Program is running")

        elif command == "help":
            print("Available commands: start, status, help, exit")

        elif command == "exit":
            print("Programm finished")
            break
