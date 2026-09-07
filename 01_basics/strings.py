# Task 1

language = "Python"

print(len(language))
print(language[0])
print(language[1])
print(language[-1])
print(language[-2])

print()

# Task 2

print(language[:2])
print(language[:3])
print(language[2:])
print(language[3:])
print(language[::2])
print(language[::-1])

print()

# Task 3

answer = input("Enter yes/no: ").strip().lower()
is_yes = answer == "yes"
print(is_yes)

print()

# Task 4

text = "Python is great. Python is simple."

print(text.count("Python"))
print(text.find("Python"))
print("Java" in text)
print(text.startswith("Python"))
print(text.endswith("simple."))
print(text.replace("Python", "Java"))

print()

# Task 5

text = "   Python    is     very   useful   "

text = text.split()
text = " ".join(text)
print(text)

text = text.replace(" ", "-")
print(text)

print()

# Task 6

value_1 = "12345"
value_2 = "Python"
value_3 = "Python3"
value_4 = "12.5"
value_5 = "   "

print(value_1.isdigit())
print(value_2.isalpha())
print(value_3.isalnum())
print(value_4.isdigit())
print(value_5.isspace())

print()

# Task 7

print("Name: Viktor\nAge: 31\nLanguage: Python")

print(r"C:\Games\World of Warcraft")
print("C:\\Games\\World of warcraft")

# Task 8

product_name = "Monitor"
price = 19999.987
quantity = 3
conversion = 0.256

total = price * quantity

print(f"Product: {product_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")
print(f"Conversion: {conversion:.1%}")

print()

# Task 9

text = input("enter text: ")

text_list = text.split()
new_text = " ".join(text_list)
print(new_text)

text_lowercase = new_text.lower()
print(text_lowercase)
text_uppercase = new_text.upper()
print(text_uppercase)
length_new_text = len(new_text)
print(length_new_text)
print(new_text[0])
print(new_text[-1])
print(new_text[::-1])
print(text_lowercase.count("python"))
print("great" in text_lowercase)
print(text_lowercase.find("python"))
print("-".join(text_list))
