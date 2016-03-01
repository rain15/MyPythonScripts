import bs4, requests

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip()


price = getEbayPrice('http://www.ebay.com/itm/MICHAEL-KORS-MK-FLEX-PUMP-MERLOT-WOMENS-SUEDE-SLIP-ON-SHOES-MULTISIZES-/221986146977?&_trksid=p2056016.m2516.l5255')

print('The price is ' + price)

    
