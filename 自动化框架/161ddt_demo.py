import unittest
from appium import  webdriver
from ddt import ddt,data
import time

@ddt
class MyTestCase(unittest.TestCase):

    #初始化
    def  setUp(self):
        desired_caps = {}
        desired_caps['platformName']   = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.102:5555'
        desired_caps['browserName'] = 'Browser'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    #释放资源
    def tearDown(self):
        self.driver.quit()