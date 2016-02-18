import re

message = 'Call me 415-555-2345 tomorrow, or at 415-555-1245.'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo.group(1))


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
moList = phoneNumRegex.findall(message)
print(moList)

