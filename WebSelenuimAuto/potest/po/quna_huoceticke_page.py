from quna.potest.base.Base import Base
from selenium.webdriver.common.keys import Keys as keys

import time
# 选择车站地址 页

class Bookticket(Base):
    #页面跳转 到 火车票
        def book_start(self):
            return self.byClassSelector(".qheader_train > a:nth-child(1) > span:nth-child(1) > b:nth-child(1)")
        #定位输入值
        def fromdiz(self):
            return self.byname("fromStation")

        def enddiz(self):
            return self.byname("toStation")

        def date(self, date):
            #清除完后写入数据
            self.byname("date").send_keys(keys.CONTROL, "a")
            self.byname("date").send_keys(keys.BACKSPACE)
            self.byname("date").send_keys(date)



        #点击搜索
        def butten(self):
            return self.byname("stsSearch")

        def sleep(self):
            time.sleep(1)



        # 1. 进入首页， 点击火车票功能（q_header_navlink）类选择器
        # 2. 输入起点站（fromStation），终点站（toStation），  日期后（date）， 点击确认（stsSearch）
        # 每次输入都要点击其他桌面，再输入

        #执行测试过程
        def booking_ticket(self, fromdiz, enddiz, date):

            self.book_start().click()
            self.sleep()

            #定位元素 输入值
            #起点
            self.fromdiz().send_keys(fromdiz)
            self.sleep()
            #终点
            self.enddiz().send_keys(enddiz)
            self.sleep()
            #日期
            self.date(date)
            self.sleep()
            #点击
            self.butten().click()




