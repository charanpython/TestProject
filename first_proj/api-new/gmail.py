# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
resp = requests.get('https://www.moviebuff.com/13-padamoodu-2009-telugu')
jsoup = BeautifulSoup(resp.content, 'html.parser')
Table = ['Name', 'Name2', 'Name3']
# print(jsoup)
jsoup = jsoup.find_all('div',attrs={'class':'department'})
for each in jsoup:
    name = each.find('h4')
    divs = each.find_all('div', attrs={'class':'row crew-group'})
    for div in divs:
        name2 = div.find('div', attrs={'class':'col-xs-4 role'}).text
        name3 = div.find('div', attrs={'class':'col-xs-8 name'}).text
        print([name.text, name2, name3])
#     print(each)
#     break
    