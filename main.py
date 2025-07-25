from pathlib import Path
import shutil
import argparse
import time

parser = argparse.ArgumentParser(description="Smart File Organiser")

parser.add_argument(
    "-f", "--folder", help="Enter the name of folder you intend to organise"
)

categories = {
    "documents": [".txt", ".pdf", ".docx", ".xlsx", ".pptx"],
    "pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "compressed": [".zip", ".rar", ".tar", ".gz"],
}

ext_to_folder = {}

args = parser.parse_args()

folder = Path(args.folder).resolve() if args.folder else Path.cwd()


if not folder.exists():
    print(f"The folder '{folder}' does not exist.")
    exit()


u_input = input("To coustomize rules enter (b), to skip (Enter): ")

user_rule = {}
if u_input == "b":
    print("Customise extension")
    ext_name = input("Extension name: ").lower().strip()
    dir_name = input("Customise folder name: ").strip()
    
    user_rule[ext_name] = dir_name

user_option = (
    input("To organise this folder once (y), to continously organise (c): ")
    .strip()
    .lower()
)

if user_option == "y":
    print("Organising the folder once...")

    for folder_name, extensions in categories.items():
        for ext in extensions:
            ext_to_folder[ext] = folder_name

        for file in folder.iterdir():
            if file.is_dir():
                continue

            ext = file.suffix.lower()

            if ext in user_rule:
                target_folder = folder / user_rule[ext]

                target_folder.mkdir(parents=True, exist_ok=True)

                destination = target_folder / file.name
                try:
                    shutil.move(str(file), str(destination))
                    print(f"Moved {file.name} to {target_folder}")
                except shutil.Error:
                    print(f"File {file.name} already exists in {target_folder}. Skipping.")


            elif ext in ext_to_folder:
                target_folder = folder / ext_to_folder[ext]

                target_folder.mkdir(parents=True, exist_ok=True)

                destination = target_folder / file.name
                try:
                    shutil.move(str(file), str(destination))
                    print(f"Moved {file.name} to {target_folder}")
                except shutil.Error:
                    print(f"File {file.name} already exists in {target_folder}. Skipping.")
    print(f"Organised {folder} successfully.")


elif user_option == "c":
    print("Continuously organising this folder...")
    print("Enter Ctrl+C to stop this process.")
    time.sleep(5)
    try:
        for folder_name, extensions in categories.items():
                for ext in extensions:
                    ext_to_folder[ext] = folder_name

        while True:
            
            for file in folder.iterdir():
                if file.is_dir():
                    continue
                ext = file.suffix.lower()

                if ext in ext_to_folder:
                    target_folder = folder / ext_to_folder[ext]

                    target_folder.mkdir(parents=True, exist_ok=True)

                    destination = target_folder / file.name
                    try:
                        shutil.move(str(file), str(destination))
                        print(f"Moved {file.name} to {target_folder}")
                    except shutil.Error:
                        print(f"File {file.name} already exists in {target_folder}. Skipping.")

            print(f"Organised {folder} successfully.")
            time.sleep(2)         

    except KeyboardInterrupt:
        print("\nContinuous organisation stopped by user.")
        exit()

else:
    print(
        "Invalid option. Please enter 'y' to organise  once or 'c' for continuous organisation."
    )
    exit()
