import requests
from bs4 import BeautifulSoup
from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ['WORD','WORDCNT']
resp = requests.get('https://www.123telugu.com/reviews/mahanati-telugu-movie-review.html')
soup = BeautifulSoup(resp.content,'html.parser')
main = soup.find('div',attrs = {'class':'main-content-post'}).text
print(main.strip())
 
for word in main.split():
    wordcnt = main.count(word)
    table.append_row([word,wordcnt])
print(table)
      