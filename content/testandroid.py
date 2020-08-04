import unittest
from time import sleep
from appium import webdriver


class MyAndroidTests(unittest.TestCase):
    def android(self):
        desired_caps = {'platformName': 'Android',  # 平台名称
                        'platformVersion': '8.1.0',  # 系统版本号
                        'deviceName': '小米平板4',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.vipkid.appengine.aiclassroomtester',  # apk的包名
                        'appActivity': 'com.vipkid.appengine.aiclassroomtester.AiClassRoomTesterMainActivity'  # activity 名称
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium

    def test_calculator(self):
        self.android()
        self.driver.get_window_size()
        self.driver.find_element_by_id("btn_scanning_auto").click()
        sleep(2)
        self.driver.find_element_by_id("enterRouter").send_keys("vkapp://appenginekit/root?url=http://172.24.28.32/test/media.html")
        self.driver.find_element_by_id("button5").click()
        sleep(10)

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()

