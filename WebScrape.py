import csv
import requests
from bs4 import BeautifulSoup as bs


URL = 'https://www.realtor.com/soldhomes'

soup = bs("req.text", 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []

COUNT = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {COUNT}'
    d['Title Name'] = title.text
    COUNT += 1
    titles_list.append(d)

FILENAME = 'titles.csv'
with open(FILENAME, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()

    w.writerows(titles_list)

# Making a GET request
r = requests.get('https://www.realtor.com/soldhomes')

# Parsing the HTML
soup = bs(r.content, 'html.parser')

images_list = []

images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})

for image in images_list:
    print(image)

# Making a GET request
r = requests.get('https://www.realtor.com/soldhomes')

# Parsing the HTML
soup = bs(r.content, 'html.parser')

s = soup.find('div', class_='entry-content')

lines = s.find_all('p')

for line in lines:
    print(line.text)
