# '''
# Created on May 24, 2018
# 
# @author: Charan
# '''
# import requests
# from bs4 import BeautifulSoup
# import re
# resp = requests.get('https://www.walmart.com/search/?query=men%20shirts&cat_id=1085632')
# jsoup = BeautifulSoup(resp.content,'html.parser')
# all_shirts = jsoup.find('ul',attrs={'class':'search-result-gridview-items'})
# for shirt in all_shirts.find_all('li')[:10]:
# #     print(shirt)
# #     break
# # #     prodTitle = shirt.find('a',attrs = {'class':"product-title-link line-clamp line-clamp-2"})
# #     prodId = shirt.find('div',attrs={'aria-label':re.compile("Walmart Number")})
# #     print(prodId)
# # #     prodPrice = shirt.find('div',attrs={'class':'product-variant-price'})
# #     print(prodPrice.text)
# #     prodColor = shirt.find('span',attrs={'class':'variants-label-text font-bold'})
# #     shipping = shirt.find('div',attrs={'class':'ShippingMessage-container color-green font-bold'})
# #     s = shipping.text if shipping is not None else None
# #     prodImage = shirt.find('img',attrs={'class':'Tile-img'})
# #     print(prodImage['src'])
# # #     break
#     prodUrl = shirt.find('a')['href']
#     
#     p='https://www.walmart.com'+ prodUrl
#     resp2 = requests.get(p)
#     print(p)
#     soup = BeautifulSoup(resp2.content,'html.parser')
#     Id = soup.find('div',attrs={'aria-label':re.compile("Walmart Number")})
#     if Id is not None:
#         print(Id['aria-label'].split(':')[1].strip())
#     
