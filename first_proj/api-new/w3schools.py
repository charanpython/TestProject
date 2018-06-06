# -*- coding:utf-8 -*-
import requests
from bs4 import  BeautifulSoup
resp = requests.get('https://www.w3schools.com/')
soup = BeautifulSoup(resp.content)
main = soup.find_all('div',attrs={'class':'w3-col l3 m6'})
# for k in main:
#     k.decompose()
#     break
# result = soup.find('div',attrs={'class':'w3-col l3 m6'})
# for k in result.find_all('a'):
#     print(k.text)
for link in main[1].find('a')['href']:
    print(link.text)
    
    [a,b,c]['a']
    
    a['a']

