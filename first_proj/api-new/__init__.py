from selenium import webdriver
import time
path = 'C:\\Users\\Charan\\Downloads\\geckodriver-v0.20.1-win64\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)
driver.get('https://www.google.com/')
driver.find_element_by_xpath('//*[@id="lst-ib"]').clear()
driver.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('abdulkalam wiki')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
time.sleep(5)
pagesource = driver.page_source
driver.quit()
print(pagesource)
