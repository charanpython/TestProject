# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
resp = requests.get('https://www.saavn.com/s/featured/hindi/Weekly_Top_Songs')
jsoup = BeautifulSoup(resp.content,'lxml')
print(jsoup)
jsoup = jsoup.find('ol',attrs={'class':'content-list'})
# print(jsoup)
# 
# all_song = jsoup.find_all('div',{'class':re.compile('details')})
# for s in all_song:
#     song = s.find('p',{'class':'song-name'})
#     print(song.text)
