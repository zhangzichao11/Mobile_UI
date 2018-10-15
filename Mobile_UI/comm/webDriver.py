from appium import webdriver
import os
import time
from comm.md_logger import myLog
import comm.md_config as myConfig

PATH = lambda p: os.path.join(os.path.split(os.path.dirname(__file__))[0], p)
countA = 1
# noinspection PyGlobalUndefined,PyRedeclaration
class webDriver:
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器驱动
        cls.driver.quit()
        # cls.driver.close()
        if countA == 3:
            myLog.logger().info('count的值 %s',countA)
            # 关闭appium服务
            os.system('start stopAppiumServer.bat')

    # noinspection PyGlobalUndefined
    @classmethod
    def setUpClass(cls):
        global driver, countA
        if countA == 1:
            # 启动appium服务
            os.system('start startAppiumServer.bat')
            time.sleep(5)
            countA = countA + 1
        # 所有的test运行前运行一次
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.1',
            'deviceName': 'Android Emulator',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True',
            'noReset': 'True',  # 如果app存在,不再重新安装
            'app': PATH('./apps/HelloFreeMusic.apk')
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
        myLog.logger().info('driver是否加载成功 %s',cls.driver)
        #cls.LIST_LATIN = "adb shell ime set com.android.inputmethod.latin/.LatinIME"
        #cls.LIST_APPIUM = "adb shell ime set io.appium.android.ime/.UnicodeIME"
