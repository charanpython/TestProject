'''
Created on May 6, 2018

@author: Charan
'''
from tabulate import tabulate
import pandas as pd
import requests
table_headers = ['ID', 'Title', 'UserId', 'Body']
Excel_data = []
resp = requests.get('https://jsonplaceholder.typicode.com/posts').json()
for ob in resp:
    id = ob['id']
    title = ob['title']
    userId = ob['userId']
    body = ob['body']
    a = [str(id),title, str(userId), body]
    Excel_data.append(a)
#print(Excel_data)
    print(a)
    print('-'.center(100,'-'))
  
  
print(tabulate(Excel_data))
 
df = pd.DataFrame(Excel_data, columns=table_headers)
# df.to_csv('test.csv')
df.to_json('test.json')