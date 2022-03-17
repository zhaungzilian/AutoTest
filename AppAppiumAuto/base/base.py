# coding=gbk
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

import time


class Base:

    def __init__(self, driver):
        self.driver = driver

    # -------------------------��λԪ��--------------------------------
    # ��λԪ�أ�������ʽ�ȴ�
    def find_el(self, *el):
        try:
            # ��ʽ�ȴ�
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(el))
            return self.driver.find_element(*el)
        except Exception as e:
            raise e

    # ��ֵ
    def find_element_send(self, value, *el):
        self.find_el(*el).clear()
        self.find_el(*el).send_keys(value)

    # ���ڴ�С
    def getwindowsize(self):
        return self.driver.get_window_size()

    # -------------------------�����¼�--------------------------------
    # ���Ϲ���
    def swipt_up(self):
        '''�ϻ�'''
        x = self.getwindowsize()["wight"]
        y = self.getwindowsize()["height"]
        return self.swipt(x / 2, y * 3 / 4, x / 2, y / 4)

    def swipt_lower(self):
        '''�»�'''
        x = self.getwindowsize()["wight"]
        y = self.getwindowsize()["height"]
        return self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4)

    def swipe_left(self, driver):
        '''��'''
        x = self.getwindowsize()["wight"]
        y = self.getwindowsize()["height"]
        return self.driver.swipe(x * 3 / 4, y / 4, x / 4, y / 4)

    def swipe_right(self, driver):
        '''�һ�'''
        x = self.getwindowsize()["wight"]
        y = self.getwindowsize()["height"]
        return self.driver.swipe(x / 4, y / 4, x * 3 / 4, y / 4)

    # Ԫ�ض�λ����
    def swiptelement(self, el, el1):
        return self.driver.scroll(el, el1)

    # ��ק�¼�
    def dragdrop(self, el, el1):
        return self.driver.drag_and_drop(el, el1)

    # appp�ر�
    def appclose(self):
        time.sleep(5)
        self.driver.close_app()
        self.driver.quit()
