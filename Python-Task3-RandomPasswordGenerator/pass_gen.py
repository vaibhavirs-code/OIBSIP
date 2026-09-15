## Random Password Generator

import random
import string
length = int(input("Enter password length (minimum 8): "))
if length < 8:
    print("Password must be at least 8 characters long.")
else:
    print("\nChoose the characters you want:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Symbols")

    choice = input("\n10" \
    "Enter at least 2 choices: ")

    characters = ""

    if "1" in choice:
        characters = characters + string.ascii_uppercase

    if "2" in choice:
        characters = characters + string.ascii_lowercase

    if "3" in choice:
        characters = characters + string.digits

    if "4" in choice:
        characters = characters + string.punctuation

    if characters == "":
        print("Please select some character types.")

    else:
        password = ""

        for i in range(length):
            password = password + random.choice(characters)

        print("\nYour generated password is:", password)