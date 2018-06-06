import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
headers = ['movie','lang','year']
data = []
data.append(headers)
resp = requests.get('https://www.moviebuff.com/directory/movies')
jsoup = BeautifulSoup(resp.content,'html.parser')
row_filter = jsoup.find_all('div',attrs={'class':'row filter-row'})
if len(row_filter) != 0:
    for k in row_filter:
        k.decompose()
jsoup = jsoup.find_all('div',attrs={'class':'row'})
if len(jsoup) != 0:
    for row in jsoup:
        for col in row.find_all('div',attrs={'class':'col-md-4'}):
            a = [k.strip() for k in col.text.split('|')]
            data.append(a)
print(tabulate(data))
        