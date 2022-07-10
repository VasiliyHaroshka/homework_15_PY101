import os


# Task №2

def file_replace() -> None:
    """
    Function for relocate files with needed format from one directory to another.
    Function requires from user current location, type files for relocation and new location for these files.
    It shows what files have been relocated and their quantity.
    :return: None
    """
    location_1: str = input("Input directory for search: ")
    form: str = input("Input which format of files you needed to relocate (e.g.: '.txt'): ")
    location_2: str = input("Input directory where you want to relocate searched files: ")
    counter: int = 0
    for file in os.listdir(location_1):
        if os.path.splitext(file)[1] == form:
            os.replace(location_1 + "\\" + file, location_2 + "\\" + file)
            print(f"File {file} from: {location_1}\ was relocated to: {location_2}\.")
            counter += 1
        else:
            pass
    print(f"{counter} files have been relocated.")


file_replace()
