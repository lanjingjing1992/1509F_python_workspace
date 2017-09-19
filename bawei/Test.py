from selenium import webdriver
import time
browser = webdriver.Firefox()

browser.get('http://172.16.10.119:8080/bwie/mhIndex.do?m=index')
browser.find_element_by_id("username").send_keys("lanjingjing")
browser.find_element_by_id("password").send_keys("442131ljj")
browser.find_element_by_link_text('登陆').click()

print('开始点名页面')
browser.find_element_by_id('treeDemo_14_a').click()




handles = browser.window_handles
browser.switch_to_window(handles[1])
time.sleep(3)

browser.find_element_by_xpath \
    ('.//*[@id=\'frm\']/div[2]/table/tbody/tr[2]/td[1]/input[1]') \
    .click()
text=browser.find_element_by_xpath('//*[@id="frm"]/div[2]/table/tbody/tr[2]/td[13]').text
print(text)
if text=='已点名':
    browser.find_element_by_xpath('//*[@id="frm"]/div[3]/table/tbody/tr/td/input[3]').click()
else:
    browser.find_element_by_xpath('//*[@id="frm"]/div[3]/table/tbody/tr/td/input[2]').click()

browser.find_element_by_xpath('.//*[@id=\'savebut\']').click()
print('完成')

time.sleep(10)
checkeds=browser.find_element_by_xpath('.//*[@id=\'frm\']/div[2]/table/tbody/tr[2]/td[1]/input[1]')
print(checkeds)


