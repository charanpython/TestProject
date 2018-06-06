
from tabulate import tabulate
import requests
from bs4 import BeautifulSoup
table_headers = ['Movie Name', 'Movie Language', 'Year']
Excel_table = []
Excel_table.append(table_headers)
resp = requests.get('https://www.moviebuff.com/directory/movies')
jsoup = BeautifulSoup(resp.content, 'html.parser')
dec = jsoup.find_all('div', attrs={'class':'row filter-row'})
if len(dec) != 0:
    for de in dec:
        de.decompose()
jsoup = jsoup.find_all('div', attrs={'class':'row'})
if len(jsoup) != 0:
    for row in jsoup:
        for col in row.find_all('div', attrs={'class':'col-md-4'}):
            a = [k.strip() for k in col.text.split('|')]
            Excel_table.append(a)
 
print(tabulate(Excel_table))    