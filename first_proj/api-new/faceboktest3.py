# -*- coding:utf-8 -*-
from selenium import webdriver
import time
path = 'C:\\Users\\Charan\\Downloads\\geckodriver-v0.20.1-win64\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)
driver.get('https://www.facebook.com/')
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('vivekanda029@gmail.com')
driver.find_element_by_name('pass').clear()
driver.find_element_by_name('pass').send_keys('vivek996655')
driver.find_element_by_id("u_0_2").click()
time.sleep(12)
pagesrc = driver.page_source
driver.close()
print(pagesrc)


