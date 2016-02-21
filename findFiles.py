import os

for folderName, subfolders, filenames in os.walk('/Users/hemapillay/Developer/PYTHON'):
        print('The folder name is ' + folderName);
        print('The subfolders are ' + str(subfolders))
        print('The file names are ' + str(filenames))
