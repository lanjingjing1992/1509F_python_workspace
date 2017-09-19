
from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://passport.cnblogs.com/user/signin')
browser.find_element_by_id("input1").send_keys("username")
browser.find_element_by_id("input2").send_keys("456123")
browser.find_element_by_id("signin").click()