# Task 1

numbers = {1, 2, 2, 3, 3, 3, 4}

print(numbers)
print(len(numbers))

print()

# Task 2

my_set = set()

print(type(my_set))

print()

# Task 3

languages = {"Python", "Go"}
languages.add("Rust")
languages.add("Python")
print(languages)

print()

# Task 4

languages = {"Python", "Go", "Rust"}

languages.remove("Go")
languages.discard("Java")

print(languages)

print()

# Task 5

allowed_commands = {"start", "stop", "status", "help"}

command = "status"

print(command in allowed_commands)

command = "restart"

print(command in allowed_commands)

print()

# Task 6

numbers = [1, 2, 2, 3, 1, 4, 4, 5]

my_set = set(numbers)
print(my_set)

print()

# Task 7

backend = {"Python", "SQL", "Git"}
devops = {"Linux", "Git", "Docker"}

my_union = backend.union(devops)
print(my_union)
my_union = backend | devops
print(my_union)

print()

# Task 8

my_intersection = backend.intersection(devops)
print(my_intersection)
my_intersection = backend & devops
print(my_intersection)

print()

# Task 9

my_difference = backend.difference(devops)
print(my_difference)
my_difference = backend - devops
print(my_difference)

my_difference = devops.difference(backend)
print(my_difference)
my_difference = devops - backend
print(my_difference)

# Task 10

my_symmetric_difference = backend.symmetric_difference(devops)
print(my_symmetric_difference)
my_symmetric_difference = backend ^ devops
print(my_symmetric_difference)

# Task 11

user_permissions = {"read", "write"}
required_permissions = {"read", "write", "delete"}

permission = required_permissions - user_permissions
print(permission)

# Task 12

required = {"read", "write"}
user_permissions = {"read", "write", "delete"}

print(required.issubset(user_permissions))

# Task 13

blocked_roles = {"banned", "suspended"}
user_roles = {"user", "premium"}

print(blocked_roles.isdisjoint(user_roles))
user_roles.add("suspended")
print(
    blocked_roles.isdisjoint(user_roles)
)  # Изменилось, потому что два множества теперь имеет одно подобное значение

# Task 14

languages = {"Python", "Go"}

languages.update({"Go", "Rust", "Java"})

print(languages)

print()

# Task 15

registered_users = {"Anna", "Alex", "Maria", "John"}
online_users = {"Alex", "Maria", "Kate"}

print(registered_users & online_users)
print(registered_users - online_users)
print(registered_users | online_users)

# Task 16

developer_a = {"Python", "Git", "SQL", "Docker"}
developer_b = {"Python", "Git", "Linux", "Kubernetes"}

print(f"Common: {developer_a & developer_b}")
print(f"Only A: {developer_a - developer_b}")
print(f"Only B: {developer_b - developer_a}")
print(f"All skills: {developer_a | developer_b}")
print(f"Different skill: {developer_a ^ developer_b}")

# Task 17

required_permissions = {"read", "write"}
user_permissions = {"read", "write", "delete"}

missing = required_permissions - user_permissions


if not missing:
    print("Access granted")
else:
    print(f"Missing permissions: {missing}")
