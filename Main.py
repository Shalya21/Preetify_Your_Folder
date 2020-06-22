import os


# This program will not change your file name in your PC.

def soldier(full_path, file_name, format_extension):
    with os.scandir(full_path) as itr:
        for entry in itr:
            if entry.is_file():
                names = entry.name
                if names != file_name and not (names.endswith(format_extension)):
                    names = names.capitalize()
                print(names)


if __name__ == '__main__':
    path = input("Enter the path of your files: ")
    file = input("Enter the file name that you don't want to change: ")
    formats = input("Enter the format that you want to  be remain unchanged: ")
    soldier(path, file, formats)
    print("The program has been executed successfully.")
