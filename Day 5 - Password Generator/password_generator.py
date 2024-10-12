import random
from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 1

# password = ""
#
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(f"Your hackable password is '{password}'")
#
# char_list = list(password)
# random.shuffle(char_list)
# randomized_string = "".join(char_list)
#
# print(f"Your harder to hack password is '{randomized_string}'")

# 2

password = []

for char in range(0, nr_letters):
    password.append(random.choice(letters))
for char in range(0, nr_symbols):
    password.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
new_password = "".join(password)

print(f"Your password is '{new_password}'")