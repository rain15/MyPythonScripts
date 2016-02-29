import bs4, requests

#res = requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')

res = requests.get('http://www.ebay.com/itm/MICHAEL-KORS-MK-FLEX-PUMP-MERLOT-WOMENS-SUEDE-SLIP-ON-SHOES-MULTISIZES-/221986146977?&_trksid=p2056016.m2516.l5255')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elems = soup.select('#prcIsum')

print(elems[0].text)


