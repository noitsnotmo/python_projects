# Use pt. 1 code to create a function that we can call and input stock symbols to output the price, change, & change percentage.
import requests
from bs4 import BeautifulSoup

# Call def & getData function with the stock symbol as the argument.
def getData(symbol):

    # Indent all below to include in function defined above.
    # Amend url with f and replace stock symbol with {symbol} to define input.
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}
    url = f'https://finance.yahoo.com/quote/{symbol}'

    # Did not need the User-Agent headers, but included anyway with headers=headers argument.
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Creates a dictionary 'stock' out of price, change, & change_percent and defines 'symbol.'
    stock = {
    'symbol': symbol,
    # Put '' around variables, changed = to :, and added commas to the ends.
    'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    'change_percent' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    }
    # Returns the stock data requested.
    return stock

print(getData('TSLA'))