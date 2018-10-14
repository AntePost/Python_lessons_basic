# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Easy, task 1
import os
import shutil


def make_dirs():
    """
    Creates directories dir_1 through dir_9.
    """
    for item in range(1, 10):
        dir_path = os.path.join(os.getcwd(), "dir_{}".format(item))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print("Folder {} already exists".format(dir_path))
    return "Folders were created successfully."


def del_dirs():
    """
    Deletes directories dir_1 through dir_9.
    """
    for item in range(1, 10):
        dir_path = os.path.join(os.getcwd(), "dir_{}".format(item))
        os.rmdir(dir_path)
    return "Folders were deleted successfully."

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Easy, task 2
def folders_in_cwd():
    """
    Shows folders in current working directory.
    """
    files_and_folders = os.listdir(path=".")
    n = 0
    for item in files_and_folders:
        if os.path.isdir(item):
            print(item)
            n += 1
    if n == 0:
        print("There are no folders in current working directory")

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# Easy, task 3
def copy_cws():
    """
    Copies current working script
    """
    copy_filename = __file__ + ".copy"
    shutil.copyfile(__file__, copy_filename)
