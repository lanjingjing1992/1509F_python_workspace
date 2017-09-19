from selenium import webdriver

drive=webdriver.Chrome()
drive.get("http://m.mail.10086.cn")#打开窗口
# drive.maximize_window()#最大化窗口
# drive.set_window_size(480,800)#设置窗口大小
drive.get('http://www.baidu.com')

drive.back()

drive.forward()
# drive.quit()#关闭窗口
