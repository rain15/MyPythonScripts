import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
result = nameRegex.findall('First Name: Mark Last Name: Smith')
print(result)

# add ? in search character class to make it non-greedy search
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<.*?>')
result = nongreedy.findall(serve)
print('\n\nNon greedy match')
print(result)


serve = '<To serve humans> for dinner.>'
greedy = re.compile(r'<.*>')
result = greedy.findall(serve)
print('\n\nGreedy match')
print(result)

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile('.*')
result = dotStar.findall(prime)
print('\nMatch all except the DOT character')
print(result)

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile('.*', re.DOTALL)
result = dotStar.findall(prime)
print('\nMatch all INCLUDING the DOT character')
print(result)

vowels = re.compile(r'[aeiou]')
result = vowels.findall('This IS all I need to know.')
print('\nMatch all vowels but oops forgot to add uppercase VOWELS')
print(result)

vowels = re.compile(r'[aeiou]', re.I) # or re.IGNORECASE
result = vowels.findall('This IS all I need to know.')
print('\nMatch all vowels including uppercase VOWELS')
print(result)
