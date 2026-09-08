# ---------------------------------------------------------
# PyPassword Generator
#
# This program generates a random password according to
# the number of letters, symbols, and numbers specified
# by the user.
#
# Steps:
# 1. Take user input for letters, symbols, and numbers.
# 2. Randomly select characters from predefined lists.
# 3. Store selected characters in a password list.
# 4. Shuffle the list to randomize character positions.
# 5. Join all characters into a single password string.
# 6. Display the generated password.
#
# Uses Python's built-in random module for randomness.
# ---------------------------------------------------------

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter= nr_letters
symbol= nr_symbols
number = nr_numbers
password = []
for char in range(1,letter+1):
   password.append(random.choice(letters))
for char in range(1,symbol+1):
    password.append(random.choice(symbols))
for char in range(1,number+1):
    password.append(random.choice(numbers))
random.shuffle(password)
print(password)
pwd=""
for char in password:
    pwd = pwd + char
print(f'your password is :- {pwd}')

