import requests
from bs4 import BeautifulSoup
# Exporting our data as a json file.
import json

# Create a list 'mystocks' to append into list 'stockdata'.
mystocks = ['AAPL', 'TSLA', 'AMC', 'NVDA']
stockdata = []

# Collapse function made in pt. 2 for organization.
def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}
    url = f'https://finance.yahoo.com/quote/{symbol}'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    stock = {
    'symbol': symbol,
    'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    'change_percent' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    }
    return stock

# Create a for loop
for item in mystocks:
    stockdata.append(getData(item))
    print('Getting: ', item)

# Use a context manager to open a new file and dump data into it. 'w' = write.
with open('stockdata.json', 'w') as f:
    json.dump(stockdata, f)

# Let us know the data set is done.
print('Done.')