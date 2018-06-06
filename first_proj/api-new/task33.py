'''
Created on May 7, 2018

@author: Charan
'''
import requests
from tabulate import tabulate
import pandas as pd
xl_data = []
table_headers = ['ALBUMID','ID','TITLE','URL']
resp = requests.get('https://jsonplaceholder.typicode.com/photos').json()
# print(resp)
for obj in resp:
#     print(obj)
    AlbumId = obj['albumId']
    Id = obj['id']
    Title = obj['title']
    Url = obj['url']
    ob_list = [AlbumId,Id,Title,Url]
#     print(ob_list)
    xl_data.append(ob_list)
#print(xl_data)
# print(tabulate(xl_data))
df = pd.DataFrame(xl_data,columns=table_headers)
# print(df)
df.to_csv('Photos.csv',index=False)



