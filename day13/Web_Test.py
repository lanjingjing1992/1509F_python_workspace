from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()

# driver.get('http://www.baidu.com')
# set=driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
# ActionChains(driver).click_and_hold(set).perform()
#
#
# btu=driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]')
# ActionChains(driver).move_to_element(btu)
# btu.click()
# time.sleep(2)
# td=driver.find_element_by_xpath('//*[@id="se-settting-1"]')
# #保存操作
# driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
# time.sleep(3)
# alert=driver.switch_to_alert()
# alert.accept()
# driver.get('http://www.baidu.com')
# setting=driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
# ActionChains(driver).click_and_hold(setting).perform()
# time.sleep(2)
# p_setting=driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]')
# ActionChains(driver).move_to_element(p_setting).perform()
# time.sleep(2)
# p_setting.click()
# driver.get('http://127.0.0.1/welcome.html')
# dbclick=driver.find_element_by_id('dbclidk')
# time.sleep(2)
# ActionChains(driver).double_click(dbclick).perform()
# alert=driver.switch_to_alert()
# time.sleep(2)
# alert.accept()
# driver.get('http://127.0.0.1/welcome.html')
# dbclick=driver.find_element_by_id('dbclidk')
# time.sleep(2)
# ActionChains(driver).double_click(dbclick).perform()
# time.sleep(2)
# alert=driver.switch_to_alert()
# alert.accept()#点击确定  自学弹出框的另外两种方法
# driver.find_element_by_link_text('baidu').click()

#name定位 id定位  classname定位 xpath定位  linktest定位 tagname定位

driver.get('http://www.baidu.com')
set_but=driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
time.sleep(2)
ActionChains(driver).click_and_hold(set_but).perform()#左键点击设置
time.sleep(2)
button=driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]')
time.sleep(2)
ActionChains(driver).move_to_element(button).perform()#移动到下拉框中的搜索设置
time.sleep(2)
button.click()
#设置不显示
time.sleep(2)
driver.find_element_by_id('s1_2').click()
#保存
driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
#处理弹出框
alert=driver.switch_to_alert()
alert.accept()