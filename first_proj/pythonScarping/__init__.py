# -*- encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
data = []
headers = ['moviename','language','year']
data.append(headers)
resp = requests.get('https://www.moviebuff.com/directory/movies')
# print(resp.content)
jsoup = BeautifulSoup(resp.content)
row_filter = jsoup.find_all('div',attrs = {'class':'row filter-row'})
# print(row_filter)
if len(row_filter) != 0:
    for k in row_filter:
        k.decompose()
jsoup = jsoup.find_all('div',attrs={'class':'row'})
if len(jsoup)!=0:
    for row in jsoup:
        for col in row.find_all('div',attrs = {'class':'col-md-4'}):
            j = [k.strip() for k in col.text.split('|')]
            data.append(j)
print(tabulate(data))
