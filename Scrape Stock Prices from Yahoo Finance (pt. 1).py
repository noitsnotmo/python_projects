# Import packages.
import requests
from bs4 import BeautifulSoup

# Create custom header (Google 'my user agent' & copy/paste string).
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}

# Create a get request using html.parser or html5lib. You can change the last letters in the link to whatever stock symbol you want.
url = 'https://finance.yahoo.com/quote/AAPL'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Create variables for current price, change, & change percentage.

# This was the original attempt, but there is a more elegant way.
# price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
# change = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).text
# change_percent = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text

# This attempt is easier to follow. It also allows me to practice indexing and using the find_all function.
price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
change_percent = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text

print(price, change, change_percent)