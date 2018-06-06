'''
Created on May 7, 2018

@author: Charan
'''
import requests
from tabulate import tabulate
import pandas as pd
table_headers = ['ID','NAME','USERNAME','EMAIL','ADDRESS','PHONE','WEBSITE','COMPANY']
xl_list = []
resp = requests.get('https://jsonplaceholder.typicode.com/users').json()
for obj in resp:
    Id = obj['id']
    Name = obj['name']
    UserName = obj['username']
    Email = obj['email']
    Address = obj['address']
    Phone = obj['phone']
    Website = obj['website']
    Company = obj['company']
    each_object = [Id,Name,UserName,Email,Address,Phone,Website,Company]
    xl_list.append(each_object)
# print(tabulate(xl_list))
df = pd.DataFrame(xl_list,columns=table_headers)
df.to_csv('users.csv',index=False)


    
    