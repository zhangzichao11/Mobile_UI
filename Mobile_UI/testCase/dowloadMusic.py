import time
#导入浏览器driver类
from comm.webDriver import webDriver
#导入界面元素类
#导入主界面元素
import pageElement.homePage as home_Page
#导入日志模块类
from comm.md_logger import myLog
#导入公共方法类
import comm.common as common
import unittest
import paramunittest
loginCase = common.get_excel_value('dowload')
@paramunittest.parametrized(*loginCase)
class loginMusic(webDriver, unittest.TestCase):
    def setParameters(self, case_Name, user_Name, user_Pwd, excepted, reMarks):
        self.case_Name = case_Name
        self.user_Name = user_Name
        self.user_Pwd = user_Pwd
        self.excepted = excepted
        self.reMark = reMarks
    def test_Login(self):
        #设置用例名称
        self._testMethodDoc = self.case_Name
        myLog.logger().info('测试用例名称:' + self._testMethodDoc)
        myLog.logger().info('测试用例说明:' + self.reMark)
        time.sleep(2)
        #判断主界面是否加载到数据
        myLog.logger().info('主页是否加载到数据 %s',home_Page.is_empty(self.driver))
        if home_Page.is_empty(self.driver):
            home_Page.click_empty(self.driver)
            time.sleep(8)
        #点击首页的Search菜单
        home_Page.click_search(self.driver)
        #点击搜索界面的搜索框
        home_Page.click_searchbg(self.driver)
        self.assertEqual(True, self.excepted)