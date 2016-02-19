import re

message = 'Call me 415-555-2345 tomorrow, or at 415-555-1245.'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo.group(1))


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
moList = phoneNumRegex.findall(message)
print(moList)

batRegex = re.compile(r'bat(man|mobile|bat)')
searchResults = batRegex.search('Batman is the best with a batmobile')
result = searchResults.group()
print(result)

batRegex = re.compile(r'Bat(wo)?man')
searchResults = batRegex.search('The adventures of Batman')
if searchResults != None:
    result = searchResults.group()
    print(result)
else:
    print("No results found.")

searchResults = batRegex.search('The adventures of Batwoman')
if searchResults != None:
    result = searchResults.group()
    print(result)
else:
    print("No results found.")



