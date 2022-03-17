from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
"""
 这里封装了selenium 基本事件 ，web驱动类型 地址， 定位元素， 鼠标事件 ， 键盘事件 
"""


class Base():
    #获取web驱动
    def __init__(self, driver):
        self.driver = driver  # type: WebDriver     #可以用这种方法标明 使用该 对象 （需要获取该对象的全局path）

    #基本定位元素
    def byname(self, byName):
       return self.driver.find_element(By.NAME, byName)

    def byId(self, byId):
        return self.driver.find_element(By.ID, byId)

    def byClassName(self, byClassName):
        return  self.driver.find_element(By.CLASS_NAME, byClassName)

    def byClassSelector(self, byClassSelector):
        return  self.driver.find_element(By.CSS_SELECTOR, byClassSelector)

    def byXpath(self, byXpath):
        return self.driver.find_element(By.XPATH, byXpath)

    def closeweb(self):
        time.sleep(3)
        self.driver.quit()

    #访问地址
    def seturl(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    #鼠标事件
    def actions(self):
        action = ActionChains(self.driver)
        #旁边点击一下
        action.move_by_offset(0, 0)
        action.context_click()
        action.perform()
