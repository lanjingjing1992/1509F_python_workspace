# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class My(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_my(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("btn_login").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp |  | 30000]]
        # driver.find_element_by_name("abc").click()
        handle=driver.current_window_handle
        all=driver.window_handles
        for h in all:
            if h!=handle:
                driver.switch_to_window(h)
        time.sleep(3)

        driver.find_element_by_xpath("/html/body/form/input[4]").click()
        driver.find_element_by_id("dbclidk").click()
        driver.find_element_by_id("dbclidk").click()
        time.sleep(3)
        self.assertEqual(u"这是一个双击事件！！！", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text("baidu").click()
        driver.find_element_by_id("forget_pwd").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
