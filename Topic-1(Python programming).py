##########################################       Task 1           #################################################

# def get_choice():
#     try:
#         choice = int(input("Enter your choice (1-3): "))
#         if choice not in [1, 2, 3]:
#             raise ValueError("Choice out of range.")
#         return choice
#     except ValueError as e:
#         print(f"Invalid input: {e}")
#         return None

# def greet_user():
#     name = input("Enter your name: ")
#     print(f"Hello, {name}!")


# from functions import get_choice, greet_user

# def main():
#     while True:
#         print("\n--- CLI App Menu ---")
#         print("1. Greet User")
#         print("2. Do Something Else")
#         print("3. Exit")

#         choice = get_choice()
#         if choice == 1:
#             greet_user()
#         elif choice == 2:
#             print("Doing something else...")
#         elif choice == 3:
#             print("Exiting program.")
#             break

# if __name__ == "__main__":
#     main()



##########################################       Task 2           #################################################

# def unit_converter():
#     print("Convert kilometers to miles")
#     try:
#         km_values = input("Enter kilometers separated by spaces: ").split()
#         km_values = list(map(float, km_values))
#         miles = list(map(lambda x: round(x * 0.621371, 2), km_values))
#         print("Miles:", miles)
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")

# if __name__ == "__main__":
#     unit_converter()







##########################################       Task 3          #################################################

# import os
# import shutil

# def copy_files(src_dir, dest_dir):
#     if not os.path.exists(dest_dir):
#         os.makedirs(dest_dir)

#     files = os.listdir(src_dir)
#     target_files = [f for f in files if f.endswith('.txt') or f.endswith('.csv')]

#     for file in target_files:
#         shutil.copy(os.path.join(src_dir, file), dest_dir)
#         print(f"Copied: {file}")

# if __name__ == "__main__":
#     source = input("Enter source directory: ")
#     destination = input("Enter destination directory: ")
#     try:
#         copy_files(source, destination)
#     except Exception as e:
#         print(f"Error: {e}")




############################################       Challenge 1     #########################################################



# def calculate():
#     try:
#         num1 = float(input("Enter first number: "))
#         op = input("Enter operator (+, -, *, /): ")
#         num2 = float(input("Enter second number: "))

#         if op == '+':
#             result = num1 + num2
#         elif op == '-':
#             result = num1 - num2
#         elif op == '*':
#             result = num1 * num2
#         elif op == '/':
#             result = num1 / num2
#         else:
#             print("Invalid operator.")
#             return

#         print("Result:", result)
#     except ValueError:
#         print("Invalid number input.")
#     except ZeroDivisionError:
#         print("Cannot divide by zero.")



# import os
# import shutil

# def organize_files():
#     folder = input("Enter directory to organize: ").strip()

#     if not os.path.isdir(folder):
#         print("Invalid directory.")
#         return

#     for file in os.listdir(folder):
#         path = os.path.join(folder, file)

#         if os.path.isfile(path):
#             ext = file.split('.')[-1]
#             target_dir = os.path.join(folder, ext + "_files")

#             if not os.path.exists(target_dir):
#                 os.makedirs(target_dir)

#             shutil.move(path, os.path.join(target_dir, file))
#             print(f"Moved {file} to {target_dir}")






# import random
# import string

# def generate_password():
#     try:
#         length = int(input("Enter password length: "))
#         chars = string.ascii_letters + string.digits + string.punctuation
#         password = ''.join(random.choice(chars) for _ in range(length))
#         print("Generated Password:", password)
#     except ValueError:
#         print("Please enter a valid number.")


# from calculator import calculate
# from organizer import organize_files
# from password_gen import generate_password

# def main():
#     while True:
#         print("\n--- CLI Toolkit ---")
#         print("1. Calculator")
#         print("2. File Organizer")
#         print("3. Password Generator")
#         print("4. Exit")

#         choice = input("Choose an option (1-4): ")

#         if choice == '1':
#             calculate()
#         elif choice == '2':
#             organize_files()
#         elif choice == '3':
#             generate_password()
#         elif choice == '4':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()

