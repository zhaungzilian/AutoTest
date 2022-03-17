import os
from appium import webdriver
import unittest
from AppuimAutoTest.commo.data_utils import getdata
from AppAppiumAuto.po.page1 import page1



class test(unittest.TestCase):

    # 运行前
    def setUp(self) -> None:
        data = getdata()
        self.appadrver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", data["desired_caps"])

        print("开始")

    # 测试完毕
    def tearDown(self) -> None:
        page1(self.appadrver).appclose()
        print("结束执行")

    def test_page1(self):
        print("过程")
        p = page1(self.appadrver)
        p.start()






if __name__ == '__main__':
    unittest.main()
