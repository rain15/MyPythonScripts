import re

secret = 'Agent Alice gave the secret documents to Agent Bob.'
searchAndReplace = re.compile('Agent \w+')
result = searchAndReplace.sub('REDACTED', secret)
print(result)

searchAndReplace = re.compile('Agent (\w)\w*')
result = searchAndReplace.sub(r'Agent \1***', secret)
print('\nUsing parameters for groupings in substitution')
print(result)

searchAndReplace = re.compile('Agent (\w)\w*', re.I | re.DOTALL | re.VERBOSE)
result = searchAndReplace.search(secret)
print('\nUsing MULTIPLE OPTIONS')
print(result)
