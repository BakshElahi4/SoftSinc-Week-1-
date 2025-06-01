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

from calculator import calculate
from organizer import organize_files
from password_gen import generate_password

def main():
    while True:
        print("\n--- CLI Toolkit ---")
        print("1. Calculator")
        print("2. File Organizer")
        print("3. Password Generator")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            calculate()
        elif choice == '2':
            organize_files()
        elif choice == '3':
            generate_password()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
