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
    # make folders and store file types according to different folders in dictionary
    folder_dictionary = categorize_files(file_types)
    sort_files(folder_dictionary)


def categorize_files(file_types):
    """make folders according to user input and store corresponding files"""
    folder_list = []
    folder_dictionary = {}
    for file_type in file_types:
        folder = input("What category would you like to sort {} files into? ".format(file_type))
        if folder not in folder_list:
            folder_list.append(folder)
            # make folder
            os.mkdir(folder)
        # store folder and the file type
        folder_dictionary[file_type] = folder
    return folder_dictionary


def sort_files(folder_dictionary):
    """Sort files based on the user's behalf' stored in dictionary"""
    for file in os.listdir("."):
        file_split = file.split(".")
        try:
            folder = folder_dictionary[file_split[1]]
            shutil.move(file, folder + "/" + file)
        except IndexError:
            pass


def get_file_types():
    """get all file types for the files and return the list"""
    file_types = []
    # get all file suffix types and store them in the list
    try:
        for file in os.listdir("."):
            file = file.split(".")
            if file[1] not in file_types:
                file_types.append(file[1])
    # ignore folders
    except IndexError:
        pass

    return file_types


main()
