from pathlib import Path
import shutil
import argparse

parser = argparse.ArgumentParser(description="Smart File Organiser")

parser.add_argument(
    "-f", "--folder", help="Enter the name of folder you intend to organise"
)
args = parser.parse_args()

folder = Path(args.folder)

document = folder / "documents"
pictures = folder / "pictures"
compressed = folder / "compressed"
financial = folder / "financial"

user_option = input("To organise this folder once (y), to continously organise (c): ").strip().lower()

if not folder.exists():
    print(f"The folder '{folder}' does not exist.")
    exit()

if user_option == 'y':
    print("Organising the folder once...")
    for file in folder.iterdir():
        if file.is_dir():
            continue
        elif file.suffix.lower() in [".txt", ".pdf", ".docx", ".xlsx", ".pptx"]:
            document.mkdir(parents=True, exist_ok=True)
            shutil.move(file, (document / file.name))

        elif file.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
            pictures.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(pictures / file.name))

        elif file.suffix.lower() in [".zip", ".rar", ".tar", ".gz"]:
            compressed.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(compressed / file.name))

        elif file.suffix.lower() in [".csv", ".xls", ".xlsx"]:
            financial.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(financial / file.name))

elif user_option == 'c':
    print("Continuously organising the folder...")
    try:
        while True:
            for file in folder.iterdir():
                if file.is_dir():
                    continue
                elif file.suffix.lower() in [".txt", ".pdf", ".docx", ".xlsx", ".pptx"]:
                    document.mkdir(parents=True, exist_ok=True)
                    shutil.move(file, (document / file.name))

                elif file.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
                    pictures.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(file), str(pictures / file.name))

                elif file.suffix.lower() in [".zip", ".rar", ".tar", ".gz"]:
                    compressed.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(file), str(compressed / file.name))

                elif file.suffix.lower() in [".csv", ".xls", ".xlsx"]:
                    financial.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(file), str(financial / file.name))
    except KeyboardInterrupt:
        print("\nExiting continuous organisation mode.")
else:
    print("Invalid option. Please enter 'y' to organise  once or 'c' for continuous organisation.")
    exit()
