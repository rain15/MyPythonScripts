

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
