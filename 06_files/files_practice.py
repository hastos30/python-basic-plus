# Task 1

from pathlib import Path
import json
import csv

base_dir = Path(__file__).resolve().parent
data_dir = base_dir / "data"

data_dir.mkdir(parents=True, exist_ok=True)

print(data_dir.name)
print(data_dir)
print(data_dir.exists())
print(data_dir.is_dir())

print()

# Task 2

notes_path = data_dir / "notes.txt"

with open(
    notes_path,
    "w",
    encoding="UTF-8",
) as file:
    file.write("Python\nGit\nLinux\nDocker\n")

with open(
    notes_path,
    "r",
    encoding="UTF-8",
) as file:
    content = file.read()

    print(content)

print()

# Task 3

with open(
    notes_path,
    "a",
    encoding="UTF-8",
) as file:
    file.write("PostgreSQL\n")

with open(
    notes_path,
    "r",
    encoding="UTF-8",
) as file:
    content = file.read()

    print(content)

print()


# Task 4

technologies = []

with open(
    notes_path,
    "r",
    encoding="UTF-8",
) as file:
    for line in file:
        technologies.append(line.rstrip())

print(technologies)

print()

# Task 5

message_path = data_dir / "message.txt"

message_path.write_text("Hello from pathlib!", encoding="utf-8")

content = message_path.read_text(encoding="utf-8")

print(content)

print()

# Task 6

report_path = data_dir / "reports" / "september.csv"

print(report_path.name)
print(report_path.stem)
print(report_path.suffix)
print(report_path.parent)

print()

# Task 7

user = {
    "name": "Alex",
    "age": 31,
    "is_active": True,
    "skills": ["Python", "Git", "Linux"],
    "middle_name": None,
}

user_path = data_dir / "user.json"

with open(
    user_path,
    "w",
    encoding="utf-8",
) as file:
    json_text = json.dumps(user, indent=4, ensure_ascii=False)
    file.write(json_text)

print()

# Task 8

with open(
    user_path,
    "r",
    encoding="utf-8",
) as file:
    loaded_user = json.load(file)

    print(type(loaded_user))
    print(loaded_user)
    print(loaded_user["skills"])
    print(loaded_user["is_active"])

# Task 9

broken_path = data_dir / "broken.json"
broken_path.write_text("{this is not valid json}", encoding="utf-8")

try:
    with open(
        broken_path,
        "r",
        encoding="utf-8",
    ) as file:
        loaded_broken = json.load(file)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("ERROR information: Format file json is not correct")

print()

# Task 10

users = [
    {"name": "Anna", "age": 25, "is_active": True},
    {"name": "Alex", "age": 17, "is_active": True},
    {"name": "Maria", "age": 31, "is_active": False},
    {"name": "John", "age": 22, "is_active": True},
]

users_path_json = data_dir / "users.json"

with open(
    users_path_json,
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        users,
        file,
        indent=4,
        ensure_ascii=False,
    )

active_users = []
adult_users = []

with open(
    users_path_json,
    "r",
    encoding="utf-8",
) as file:
    loaded_users = json.load(file)

    for user in loaded_users:
        if user["is_active"]:
            active_users.append({user["name"], user["age"], user["is_active"]})

        if user["age"] >= 18:
            adult_users.append({user["name"], user["age"], user["is_active"]})


print(f"Active users: {active_users}")
print(f"Adult users: {adult_users}")

print()

# Task 11

users_path_csv = data_dir / "users.csv"
fieldnames = ["name", "age", "is_active"]

with open(
    users_path_csv,
    "w",
    encoding="utf-8",
    newline="",
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
    )

    writer.writeheader()
    writer.writerows(users)

print()
