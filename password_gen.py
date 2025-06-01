import random
import string

def generate_password():
    try:
        length = int(input("Enter password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")
