#! /usr/bin/env python3

import re, pyperclip

#test input file is at http://iifs.adhe.edu/proposals/pdfs/Agency/directory.pdf

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-222-4567, 234-2444, (415)234-2344, 234-2344 ext 23445, ext. 12344, x23455

(
((\d\d\d)|(\(\d\d\d\)))?        #area code (optional)
(\s|-)        # first separator
\d\d\d        # first 3 digits
-       # separator
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)        # extension word-part (optional)
(\d{2,5}))? # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

#print(extractedPhone) #for testing
#print(extractedEmail) #for testing

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)




