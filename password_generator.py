import random
import string

def generate_password(length_local):
    special_characters = '!#$%&,-./<>?@_'
    characters = string.ascii_letters + string.digits + special_characters
    return ''.join(random.choice(characters) for _ in range(length_local))

try:
    length = int(input("Enter password length: "))
    if length < 8:
        print("Password length should be at least 8 characters.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")