#-*- coding:utf-8 -*- 
'''
Created on May 18, 2018

@author: Charan
'''

from selenium import webdriver
# browser = webdriver.Firefox()

path="C:\\Users\\Charan\\Downloads\\geckodriver-v0.20.1-win64\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)
driver.get('https://emicalculator.net/')
driver.find_element_by_xpath('//*[@id="loanamount"]').clear()
driver.find_element_by_xpath('//*[@id="loanamount"]').send_keys(200000)
driver.find_element_by_tag_name('body').click()
driver.find_element_by_xpath('//*[@id="loaninterest"]').clear()
driver.find_element_by_xpath('//*[@id="loaninterest"]').send_keys(13)
driver.find_element_by_tag_name('body').click()
driver.find_element_by_xpath('/html/body/div/div/main/article/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[1]/a').click()
pagesource = driver.page_source
driver.close()
print(pagesource)