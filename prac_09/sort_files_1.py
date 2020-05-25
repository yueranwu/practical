"""
CP1404 practical 09
Use python os and shutil to sort files
"""

import os
import shutil


def main():
    """Sort file according to their file suffix"""
    # access to the file folder
    os.chdir("FilesToSort")
    # get all types of the file suffix
    file_types = get_file_types()
    # create folders according to the types of suffix
    make_folders(file_types)
    sort_files()


def sort_files():
    for file in os.listdir('.'):
        file_split = file.split(".")
        try:
            shutil.move(file, file_split[1] + "/" + file)
        except IndexError:
            pass


def make_folders(file_types):
    """make folders with suffix"""
    try:
        for file_type in file_types:
            os.mkdir(file_type)
    # pass when the file is already created
    except FileExistsError:
        pass


def get_file_types():
    """get all file types for the files and return the list"""
    file_types = []
    # get all file suffix types and store them in the list
    try:
        for file in os.listdir('.'):
            file = file.split(".")
            if file[1] not in file_types:
                file_types.append(file[1])
    # ignore folders
    except IndexError:
        pass

    return file_types


main()
