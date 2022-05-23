import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org/page/1/'

req = requests.get(URL)
soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs = {'class','head'})

print(titles[4].text)
