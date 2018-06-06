# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
xl_data = []
table_headers = ['ACTOR','ROLE']
resp = requests.get('https://www.moviebuff.com/13-padamoodu-2009-telugu')
soup = BeautifulSoup(resp.content,'html.parser')

#----------------------Crew Data------------------------------------
jsoup = soup.find('div',id="cast")
for each in jsoup.find_all('div',attrs={'class':'col-xs-6 col-sm-4 credit'}):
    name = each.find('div',attrs={'class':'name'})
    role = each.find('div',attrs={'class':'role'})
    a = [name.text if name is not None else None, role.text if role is not None else None]
    xl_data.append(a)
print(xl_data)

#-------------------------Technical Details---------------------------
ksoup = soup.find('div',id='technicaldetails')
if ksoup is not None:
    for each in ksoup.find_all('div',attrs={'class':'row secondary-info'}):
        Technical = each.find('div',attrs={'class':'col-sm-4'})
        Deatails = each.find('div',attrs={'class':'col-sm-8'})
        a = [Technical.text if Technical is not None else None,Deatails.text if Deatails is not None else None]
        xl_data.append(a)
# print(tabulate(xl_data))
df = pd.DataFrame(xl_data,columns=table_headers)
df.to_csv('technical.csv',index=False)


    
    