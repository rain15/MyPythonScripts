

helloFile = open('/Users/.../MyPythonScripts/hello.txt')
content = helloFile.read()
print(content)

helloFile.readlines() # returns contents in list data structure form
helloFile.close()

helloFile = open('/Users/<addyourdir>/MyPythonScripts/hello.txt', 'a') # a = append, w = overwrite
helloFile.write('Hello,  I am appending more text here!!')
helloFile.close()

#To store data structures' values in a file,  use shelve module
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()


shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

shelfFile.close()

import shutil #to copy, move, create, delete files and directories.

shutil.copy('/usr/bin/test.py', '/Users/defaultuser')
shutil.copy('/usr/bin/testdir', '/Users/defaultuser/testdir_backup')

#delete files and directories - number of ways

os.unlink('hello.txt')

os.rmdir('/Users/Guest/MyPythonScripts') #removes directory only if it's empty

import shutil
shutil.rmtree('/Users/Guest/MyPythonScripts') #removes directory even if it has files in it.

########################
import os

os.chdir('/Users/Guest/MyPythonScripts')

for filename in os.listdir():
    if (filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename) # test this code worked before deleting all the files.


# to send the files to trash bin just incase you want to recover them,
#install send2trash module using pip module

import send2trash
send2trash.send2trash('.txt')

#Walking a directory tree - say you want to get all files inside a folder that
# has sub folders.
import os

for folderName, subfolders, filenames in os.walk('/Users/hemapillay/MyPythonScripts'):
        print('The folder name is ' + folderName);
        print('The subfolders are ' + str(subfolders))
        print('The file names are ' + str(filenames))
        

        
        
