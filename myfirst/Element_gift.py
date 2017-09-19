from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import urllib

driver = webdriver.Firefox()
driver.get('http://127.0.0.1')
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('btn_login').click()

try:
    a=driver.switch_to_alert().text
    print(a)

except:
    soup = BeautifulSoup(driver.page_source, "html.parser")
content = soup.select('h1')
for i in content:
       print(i.text)
