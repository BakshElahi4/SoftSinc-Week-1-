import os
import shutil

def organize_files():
    folder = input("Enter directory to organize: ").strip()

    if not os.path.isdir(folder):
        print("Invalid directory.")
        return

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            ext = file.split('.')[-1]
            target_dir = os.path.join(folder, ext + "_files")

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            shutil.move(path, os.path.join(target_dir, file))
            print(f"Moved {file} to {target_dir}")
