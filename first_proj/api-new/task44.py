'''
Created on May 7, 2018

@author: Charan
'''
import requests
from tabulate import tabulate
import pandas as pd
formatted_data = []
headers = ['USERID','ID','TITLE','COMPLETED_STATUS']
resp = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# print(resp)
for obj in resp:
    UserId = obj['userId']
    Id = obj['id']
    Title = obj['title']
    Completed_Status = obj['completed']
    each_object = [UserId,Id,Title,Completed_Status]
    formatted_data.append(each_object)
# print(tabulate(formatted_data))
df = pd.DataFrame(formatted_data,columns=headers)
# print(df)
df.to_csv('Todos.csv')
     