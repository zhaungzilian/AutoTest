from quna.potest.base.Base import Base

# 购买票页面
# 1. 负责点击购票

class Buy(Base):
    def buy_butten(self):
       return self.byXpath("/html/body/div[4]/div/div[1]/ul[2]/li[1]/div/div[7]/a[1]")


    #编写测试过程
    def buy_start(self):
        self.buy_butten().click() #点击购买

