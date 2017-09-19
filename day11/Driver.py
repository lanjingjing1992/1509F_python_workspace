from selenium import webdriver#从selenium引入web驱动
import time
driver=webdriver.Firefox()#设置火狐驱动
driver.get('http://127.0.0.1')#打开网址
time.sleep(2)#休眠2秒
driver.find_element_by_id('username').send_keys('zhangxu')#根据id获取到名字的输入框并且填入姓名
time.sleep(2)#休眠2秒
driver.find_element_by_id('password').send_keys('1234')#根据id获取到密码的输入框并且填入密码
time.sleep(2)#休眠2秒
driver.find_element_by_id('btn_login').click()#根据id获取到登陆按钮的输入框并且点击
time.sleep(2)#休眠2秒


