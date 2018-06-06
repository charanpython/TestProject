# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
resp = requests.get('https://www.moviebuff.com/13-padamoodu-2009-telugu')
jsoup = BeautifulSoup(resp.text,'lxml')
# print(jsoup)
jsoup = jsoup.find_all('div',attrs={'class':'department'})
for each in jsoup:
#     print(each)
#     print('-'.center(120,'-'))
    department = each.find('h4')
    print(department.text)
    roles = each.find_all('div',attrs={'class':'col-xs-4 role'})
print(roles)

    
    
