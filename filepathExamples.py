import os

os.path.join('user', 'bin', 'env', 'file.png')
os.sep

os.getcwd()
os.chdir('/Users/<user>/MyPythonScripts')

os.path.abspath('spam.png')

os.path.isabs('../../spam.png') #will return false as ../.. is relative

os.path.isabs('/Users/guestuser/MyPythonScripts') #will return true

os.path.relpath('/Users/guestuser/MyPythonScripts', '/Users/guestuser')

os.path.dirname('/Users/guestuser/MyPythonScripts/test.png')
os.path.basename('/Users/guestuser/MyPythonScripts/test.png') #returns filename, the last part which is test.png
                 
os.path.exists('/Users/guestuser/MyPythonScripts/test.png')

os.path.isfile('/Users/guestuser/MyPythonScripts/test.png')
os.path.isdir('/Users/guestuser/MyPythonScripts/test.png')

os.path.getsize('/Users/guestuser/MyPythonScripts/test.png')

os.listdir('/Users/guestuser/MyPythonScripts')

os.listdir('/Users/hemapillay/MyPythonScripts')

os.makedirs('/Users/hemapillay/MyPythonScripts/newdirectory')

os.makedirs('../newdirectory')

#get total size of files in a given directory
totalSize = 0
dirName = '/Users/guestuser/MyPythonScripts'
for fileName in os.listdir(dirName):
    if not os.path.isfile(os.path.join(dirName, fileName)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(dirName, fileName))
    
print(totalSize)
