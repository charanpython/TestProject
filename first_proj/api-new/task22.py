'''
Created on May 7, 2018

@author: Charan
'''
import requests
from tabulate import tabulate
import pandas as pd
data = []
table_headers = ['USERID','ID','TITLE']
resp = requests.get('https://jsonplaceholder.typicode.com/albums').json()
# print(resp)
for obj in resp:
    UserId = obj['userId']
    Id = obj['id']
    Title = obj['title']
    a = [UserId,Id,Title]
#    print(a)
    data.append(a)
# print(data)
#print(tabulate(data))
df = pd.DataFrame(data,columns=table_headers)
print(df)
# df.to_csv('albums.csv',index=False)

    