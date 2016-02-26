import webbrowser, sys, pyperclip

sys.argv #['mapit.py', '800', 'N, 'Point', 'St']

# Check if command line arguments were passed

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print('address is ' + address)
webbrowser.open('https://www.google.com/maps/place/' + address)
