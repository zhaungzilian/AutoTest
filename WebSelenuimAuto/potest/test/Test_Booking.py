from WebSelenuimAuto.potest.po.quna_goma_pagei import Buy
from WebSelenuimAuto.potest.po.quna_huoceticke_page import Bookticket
from WebSelenuimAuto.potest.commo.read_excel import read_xlsx, date_today
from selenium import webdriver
import pytest

data = read_xlsx("../data/test.xlsx", 0, True)

class TestBooking():

     # 导入 两个测试页面进行测试
     @pytest.mark.parametrize(["fromdiz", "enddiz", "n"], data)
     def test_1(self,fromdiz, enddiz, n):
         # 测试搭建
        self.driver = webdriver.Firefox()
        url = "https://www.qunar.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        print("开始执行")

        ticke = Bookticket(self.driver)
        #三个参数， 起点， 终点， 日期
        ticke.booking_ticket(fromdiz, enddiz, date_today(n))

        #跳转到购买页面，点击购买
        buy = Buy(self.driver)
        buy.buy_start()

        self.driver.quit()

        print("退出")




if __name__ == '__main__':
    pytest.main(["-s", "Test_Booking.py"])

#测试的参数说明
# -m=xxx: 运行打标签的用例
# -reruns=xxx，失败重新运行
# -q: 安静模式, 不输出环境信息
# -v: 丰富信息模式, 输出更详细的用例执行信息
# -s: 显示程序中的print/logging输出
# --resultlog=./log.txt 生成log
# --junitxml=./log.xml 生成xml报告

