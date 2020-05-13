import os
import re
import shutil

def renameFiles(path, files, nameFile):
    # function to rename files
    count = 0
    for i in range(len(files)):
        if re.search(fr"^{nameFile}", files[i])==None:
            old_name = os.path.join(path, files[i])
            new_name = os.path.join(path, f'{nameFile}_{str(i)}.jpg')
            os.rename(old_name, new_name)
            count += 1
    return f"Number of files that have been renamed: {count}"

def moveFiles(old_path,files_in_path, new_path):
    count = 0
    for file in files_in_path:
        shutil.move(os.path.join(old_path, file), os.path.join(new_path, file))
        count += 1
    return print(f"Number of files that have been moved: {count}")