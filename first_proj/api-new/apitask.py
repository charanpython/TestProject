'''
Created on May 6, 2018

@author: Charan
'''

import requests
from tabulate import tabulate
import pandas as pd
new_data = []
table_headers = ['PostId','Id','Name','Email','Body']
resp = requests.get('https://jsonplaceholder.typicode.com/comments').json()
# print(resp)

for obj in resp:
#     print(obj)
#     print('-'.center(150,'-'))
   
    PostId = obj['postId']
    Id = obj['id'] 
    Name = obj['name']
    Email = obj['email']
    Body = obj['body']
    table_colums = [str(PostId),str(Id),Name,Email,Body]
#     print(table_colums)
    new_data.append(table_colums)
# print(new_data)
    
# print(tabulate(new_data)
df = pd.DataFrame(new_data,columns=table_headers)
# df.to_csv('comments1.csv',index=False)
df.to_json('comments.json')


    
