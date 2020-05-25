"""
CP1404/CP5632 Practical
Reformat file names
"""
import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for file in filenames:
            # join the path
            path = os.path.join(directory_name, file)
            # get new name
            new_name = os.path.join(directory_name, get_fixed_filename(file))
            # replace new name with old name
            os.rename(path, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    # iterate through each character in the name
    for index, char in enumerate(name):
        new_name += char
        try:
            # reformat through adding underscore
            if name[index].islower() and name[index + 1].isupper():
                new_name += "_"
            # reformat through changing the first letter after underscore to uppercase
            elif name[index] == "_" and name[index + 1].islower():
                name[index + 1].upper()

        # handle index error
        except IndexError:
            pass

    return new_name


main()
