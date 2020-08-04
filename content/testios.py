import unittest
from time import sleep

from appium import webdriver


class MyIosTests(unittest.TestCase):

    def ios(self):
        desired_caps = {
                            "deviceName": "ipad",
                            "platformName": "iOS",
                            "platformVersion": "13.5.1",
                            "bundleId": "com.vipkid.aiclassroom",
                            "udid": "00008020-001D25D01AE1002E"

                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium

    def test_calculator(self):
        self.ios()
        self.driver.get_window_size()
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="Flutter"]').click()
        sleep(2)
        # self.driver.find_element_by_id("enterRouter").send_keys("vkapp://appenginekit/root?url=http://172.24.28.32/test/media.html")
        # self.driver.find_element_by_id("button5").click()
        #
        # sleep(10)

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()

