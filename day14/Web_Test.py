from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get('http://blog.csdn.net/')#打开csdn网址
driver.maximize_window()#窗口最大化
time.sleep(3)
login=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[1]/a[1]')
ActionChains(driver).click_and_hold(login).perform()
time.sleep(2)
login.click()#点击登陆按钮
# driver.get('https://passport.csdn.net/account/login?ref=toolbar')
qq=driver.find_element_by_xpath('//*[@id="qqAuthorizationUrl"]')
qq.click()

time.sleep(4)
driver.switch_to_frame('ptlogin_iframe')
qq_login=driver.find_element_by_xpath('//*[@id="qlogin_list"]/a[1]')
qq_login.click()#点击头像登陆
time.sleep(5)
driver.switch_to_default_content()
img=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[6]')
ActionChains(driver).click_and_hold(img).perform()
time.sleep(1)
name=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[6]/div/div/div[2]/dl/dd/a')

print(name.text)#打印昵称
#设置
setting=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[6]/div/div/div[3]/a[1]')
ActionChains(driver).move_to_element(setting)
setting.click()
time.sleep(3)
 #窗口跳转‘
current=driver.current_window_handle#获取缓存中所有的窗口
all=driver.window_handles
for handle in all:
    if handle!=current:#对于所有窗口中不等于当前窗口的即为将要跳转的窗口
        driver.switch_to_window(handle)#跳转窗口
#个人隐私设置
person_setting=driver.find_element_by_xpath(''
                                            '//*[@id="main"]/div/div[2]/a[3]')
ActionChains(driver).move_to_element(person_setting).perform()
person_setting.click()
inputs=driver.find_elements_by_tag_name('input')#通过标签查找一组选择框
for input in inputs:
    text=input.get_attribute('value')#获取到这组每一个控件的value
    #将value=0的勾选，也就是第一个选择框
    if text==0:
        input.click()

driver.find_element_by_xpath('//*[@id="main"]/div/form/div/input').click()#保存修改
time.sleep(3)
alert=driver.switch_to_alert()
alert.accept()#对于弹出框选择确定