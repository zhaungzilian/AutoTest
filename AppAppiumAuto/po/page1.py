from AppAppiumAuto.base.base import Base
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time


class page1(Base):

    def start(self):
        wlan = self.find_el(By.XPATH, "//*[@text='WLAN']")
        yingyon = self.find_el(By.XPATH, "//*[@text='应用']")

        action = TouchAction(self.driver)

        print("正在移动")
        action.press(yingyon).wait(500).move_to(wlan)
        action.release()
        action.perform()

        print("点击安全")
        self.find_el(By.XPATH, "//*[@text='安全']").click()

        self.find_el(By.XPATH, "//*[@text='屏幕锁定']").click()

        self.find_el(By.XPATH, "//*[@text='图案']").click()


        time.sleep(2)
        action.press(x=210, y=910).wait(200).move_to(x=549, y=910).wait(200).move_to(x=870, y=910)\
            .move_to(x=549, y=1239).wait(200)\
            .move_to(x=210, y=1556).wait(200).move_to(x=549, y=1556).wait(200).move_to(x=870, y=1556)

        action.release()
        action.perform()

