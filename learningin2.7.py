import os

def rename_files():
    #(1) get the file names from a given folder
    file_list = os.listdir(r"C:\Users\scept\Downloads\prank")
    print(file_list)
    os.chdir(r"C:\Users\scept\Downloads\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
rename_files()