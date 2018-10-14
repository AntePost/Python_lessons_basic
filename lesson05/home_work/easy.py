import os


def change_dir(dir_name):
    """
    Changes directory.
    """
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(dir_path):
        os.chdir(dir_name)
        return "We're now in folder {}".format(dir_name)
    else:
        return "Impossible to move there"


def content_in_cwd():
    """
    Shows files and folders in the current working directory.
    """
    print("Files and folders in the current directory:")
    files_and_folders = os.listdir(path=".")
    for item in files_and_folders:
        print(item)


def del_dir(dir_name):
    """
    Deletes the chosen folder.
    """
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(dir_path):
        os.rmdir(dir_path)
        return "Folder was deleted successfully."
    else:
        return "Impossible to delete"


def make_dir(dir_name):
    """
    Creates a folder.
    """
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        return "Folder was created successfully."
    except FileExistsError:
        return "Folder with this name already exists"
