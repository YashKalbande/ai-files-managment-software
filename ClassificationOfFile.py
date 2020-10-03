import os
import glob

user_input = input("Enter the path of your file: ")
os.chdir(user_input)
# glob function of glob module to detect all files inside current directory
files_list = glob.glob("*")
# Creating a set of extension type inside the folder to avoid duplicate entries
extension_set = set()
# Add each type of extension to the set
current_dir = os.getcwd()
for file in files_list:
    extension = file.split(sep=".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue


def create_dirs():
    for dir in extension_set:
        try:
            os.makedirs(dir+"_files")

        except FileExistsError:
            continue


# Create function to move files to respective folders
def arrange():
    for file in files_list:
        fextension = file.split(sep=".")
        try:
            os.rename(file, fextension[1]+"_files/"+file)
        except(OSError, IndexError):
            continue




