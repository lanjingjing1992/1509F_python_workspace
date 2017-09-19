from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
# driver.get('https://qzone.qq.com/')
# driver.switch_to_frame('login_frame')#进入到登陆的iframe层
# driver.find_element_by_id('switcher_plogin').click()#找到通过账号密码登陆的id，并且点击
# driver.find_element_by_id('u').send_keys('2364365304')#找到姓名的id并且赋值
# driver.find_element_by_id('p').send_keys('123456')#找到密码的id并且赋值
# driver.find_element_by_id('login_button').click()#点击登陆按钮
# driver.get('http://www.baidu.com')
# driver.set_window_size(480,800)#设置浏览器的大小
# #
# time.sleep(2)#休眠2秒
# driver.maximize_window()#浏览器最大化
# driver.get('http://127.0.0.1')#打开另外一个登陆网页
# time.sleep(2)#休眠2秒
# driver.back()#浏览器后退到百度页面
# driver.forward()#前进到登陆页面
# driver.get('http://www.baidu.com')
# editext=driver.find_element_by_class_name('s_ipt')
# editext.send_keys('支付宝')#在百度的输入框内输入支付宝
# attribute=editext.get_attribute('autocomplete')#输入框的属性
# print(attribute)
# size=editext.size#百度输入框的大小
# print(size)
# button=driver.find_element_by_id('su')
# button.click()#点击搜索
# driver.get('https://pan.baidu.com/')#打开百度网盘
# time.sleep(3)
# login=driver.find_element_by_class_name('account-title').find_element_by_tag_name('a')
# print(login)
# login.click()
# driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('15901337131')
# driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('442131ljj')
# driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
# driver.get('https://qzone.qq.com/')#打开qq空间的网址
# time.sleep(2)
# driver.switch_to_frame('login_frame')#进入到iframe层
# login=driver.find_element_by_id('switcher_plogin')#账号密码登陆
# login.click()#点击
# username=driver.find_element_by_id('u')#通过id查找到用户名输入框
# username.send_keys('2364365304')#在用户名输入框输入账号
# password=driver.find_element_by_id('p')#通过id查找到用密码输入框
# password.send_keys('123456')#输入密码
# button=driver.find_element_by_id('login_button')#点击登陆按钮
# button.click()
driver.get('http://www.baidu.com')
time.sleep(3)
# driver.find_element_by_name('tj_login').click()
# above=driver.find_element_by_name('tj_login')
# ActionChains(driver).move_to_element(above).perform()
# ActionChains(driver).click(above).perform()
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()





