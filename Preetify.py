import os


# This program will make changes in your system files.
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1


if __name__ == '__main__':
    path = input("Enter the path of the files that you want to capitalize: ")
    file = input("Enter the path of the file that you want to keep unchanged: ")
    formats = input("Enter the extension of format taht you want to rename with digits")
    soldier(path, file, formats)
