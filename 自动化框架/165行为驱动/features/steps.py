from lettuce import *
from appium import webdriver

@before.each_scenario
def launchApp(scenario):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.102:5555'
    desired_caps['appPackage'] = 'com.android.calculator2'
    desired_caps['appActivity'] = '.Calculator'
    desired_caps['unicodeKeyboard'] = "True"
    desired_caps['resetKeyboard'] = "True"

    world.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

@after.each_scenario
def closeApp(scenario):
    world.driver.quit()

@step("I have two number : (\d+) and (\d+)")
def have2number(step,number1, number2):
    world.number1 = number1
    world.number2 = number2

@step("Do add method")
def doAdd(step):
    numa = world.driver.find_element_by_id("digit_"+world.number1)
    numa.click()

    numa = world.driver.find_element_by_id("op_add")
    numa.click()

    numa = world.driver.find_element_by_id("digit_"+world.number2)
    numa.click()

    numa = world.driver.find_element_by_id("eq")
    numa.click()

    world.result = world.driver.find_element_by_class_name("android.widget.EditText").text

@step("I get result : (\d+)")
def judgeResult(step,result):
    assert result == world.result,"The result are not euqal %s and %s"% result and world.result
