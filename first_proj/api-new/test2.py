# -*- coding:utf-8 -*-
from selenium import webdriver
import time
path = 'C:\\Users\\Charan\\Downloads\\geckodriver-v0.20.1-win64\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)
driver.get('https://www.youtube.com/')
driver.find_element_by_name('search_query').clear()
driver.find_element_by_name('search_query').send_keys('coery schafer')
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon').click()
time.sleep(20)
pagesource = driver.page_source
driver.close()
print(pagesource)
