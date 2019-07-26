from appium import webdriver
import time

#定义初始化的属性信息
desired_caps = {}
desired_caps['platformName'] = 'Android'   #platformName,目标设备平台Android/iOS
desired_caps['platformVersion'] = '5.1'   #platformVersion,目标设备的平台版本
desired_caps['deviceName'] = '810EBM32TZ4K'   #deviceName,目标设备名称
desired_caps['browseName'] = 'Browser'
desired_caps['unicodeKeyboard'] = 'True'   #unicodeKeyboard,是否使用Appium 输入法
desired_caps['resetKeyboard'] = 'True'   #resetKeyboard,是否恢复默认键盘
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#打开首页
driver.get("http://www.imooc.com")
time.sleep(3)

#验证实战标签显示
e = driver.find_element_by_xpath('//*[@id="middle"]/section[2]/ul/li[3]/a')

#断言显示了
assert e.is_displayed()
#关闭
driver.quit()

