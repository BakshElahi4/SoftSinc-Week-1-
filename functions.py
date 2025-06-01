def get_choice():
    try:
        choice = int(input("Enter your choice (1-3): "))
        if choice not in [1, 2, 3]:
            raise ValueError("Choice out of range.")
        return choice
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
