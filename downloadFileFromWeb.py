import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

if res.status_code == 200:
    print(res.text[:500])

# function below raises exception if file not found on web.
res.raise_for_status()

# Python and unicode - http://nedbatchelder.com/text/unipain.html

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()



