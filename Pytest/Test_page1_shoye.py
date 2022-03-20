import time
import pytest
import logging
from Pytest.comme.LoggerUtils import logs

# logutis = logging.getLogger(__name__)

logutis = logs()



@pytest.fixture(scope='function', params='' , ids='', name='')
def fixture():
    print("前置")
    yield
    print("后置")

class TestPage1():



    def test_start1(self):
        logutis.info("测试用1日志")
        print("test_start1........")

    def test_start2(self):
        logutis.info("测试用2日志")
        print("test_start2........")

    def test_start3(self, fixture):
        logutis.info("测试用3日志")
        print("test_start3........")



if __name__ == '__main__':
    pytest.main(["-vs"])