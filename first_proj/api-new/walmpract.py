import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
walmartt = []
table_heads = ['PRODNAME','PRICE','SHIPMENTBY','PRODIMG','PRODURL']
resp = requests.get('https://www.walmart.com/search/?query=men%20shirts&cat_id=1085632')
jsoup = BeautifulSoup(resp.content,'html.parser')
main_cont = jsoup.find('ul',attrs={'class':'search-result-gridview-items'})
for shirt in main_cont.find_all('li')[:9]:
    prodTitle = shirt.find('a',attrs={'class':'product-title-link line-clamp line-clamp-2'})
#     print(prodTitle.text)
    prodPrice = shirt.find('div',attrs={'class':'price-main-block'})
#     print(prodPrice.text)
    ship_By = shirt.find('span',attrs={'class':'marketplace-sold-by-company-name'})
    mark_By = ship_By.text if ship_By is not None else None
#     print(mark_By)
    prod_Img = shirt.find('img',attrs={'class':'Tile-img'})
#     print(prod_Img['src'])
    prod_Url = shirt.find('a')['href']
    Url = 'https://www.walmart.com'+prod_Url
    result = [prodTitle.text,prodPrice.text,mark_By,prod_Img['src'],Url]
    walmartt.append(result)
# print(tabulate(walmartt))
df = pd.DataFrame(walmartt,columns=table_heads)
df.to_csv('walmart.csv',index=False)
    
    