'''
Created on May 25, 2018

@author: Charan
'''
import os
import io
from PIL import Image
import requests
from bs4 import BeautifulSoup


downld_location = "C:\\Users\\Charan\\Desktop\\IMAGES\\"
folder_name = "24_moviepics"
if not os.path.isdir(downld_location+folder_name):
    os.mkdir(downld_location+folder_name)
path = downld_location+folder_name+'\\'+folder_name


resp = requests.get('https://www.moviebuff.com/24-2016-telugu')
jsoup = BeautifulSoup(resp.content,'html.parser')
images = jsoup.find_all('img')
for image in images:
    pic = requests.get(image['src'])
    image_file = io.BytesIO(pic.content)
    imag = Image.open(image_file)
    imag.save(path)
