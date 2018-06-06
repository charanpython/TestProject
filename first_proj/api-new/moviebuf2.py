'''
Created on May 22, 2018

@author: Charan
'''
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
title_headers = ["TECHNICAL","DEATAILS"]
xl_data = []
resp = requests.get('https://www.moviebuff.com/13-padamoodu-2009-telugu')
jsoup = BeautifulSoup(resp.content,'html.parser')
jsoup = jsoup.find('div',id='technicaldetails')
if jsoup is not None:
    for each in jsoup.find_all('div',attrs={'class':'row secondary-info'}):
        Technical = each.find('div',attrs={'class':'col-sm-4'})
        Deatails = each.find('div',attrs={'class':'col-sm-8'})
        a = [Technical.text,Deatails.text]
        xl_data.append(a)
# print(tabulate(xl_data))
df = pd.DataFrame(xl_data,columns=title_headers)
df.to_csv('technical.csv',index=False)
    