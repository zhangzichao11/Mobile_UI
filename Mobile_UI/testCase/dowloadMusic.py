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
class dowloadMusic(webDriver, unittest.TestCase):

    def setParameters(self, case_Name, user_Name, user_Pwd, search_data, excepted, reMarks):
        self.case_Name = case_Name
        self.user_Name = user_Name
        self.user_Pwd = user_Pwd
        self.search_data = search_data
        self.excepted = excepted
        self.reMark = reMarks
    def test_Dowload(self):
        #设置用例名称
        self._testMethodDoc = self.case_Name
        myLog.logger().info('测试用例名称:' + self._testMethodDoc)
        myLog.logger().info('测试用例说明:' + self.reMark)
        time.sleep(2)
        #判断主界面是否加载到数据
        if home_Page.is_empty(self.driver):
            #数据加载失败的截屏
            common.Screenshot1(self.driver)
            home_Page.click_empty(self.driver)
            time.sleep(8)
        #点击首页的Search菜单
        home_Page.click_search(self.driver)
        #点击搜索界面的搜索框
        home_Page.click_searchbg(self.driver)
        #搜索界面的截屏
        common.Screenshot1(self.driver)
        #输入要搜索的内容
        myLog.logger().info('搜索内容 %s',self.search_data)
        home_Page.search_input(self.driver,self.search_data)
        #点击youtube搜索工具条
        home_Page.click_youtube(self.driver)
        time.sleep(3)
        #滑动屏幕进行,查找要点击的内容
        common.swipeUp1(self.driver,1)
        #点击要播放的视频
        home_Page.click_video(self.driver)
        time.sleep(3)
        #等待视频播放完成
        time.sleep(home_Page.get_time(self.driver))
        common.Screenshot1(self.driver)
        home_Page.click_back(self.driver)
        home_Page.click_back(self.driver)
        home_Page.click_back(self.driver)
        home_Page.click_home(self.driver)
        #主界面是否有下载的截屏
        common.Screenshot1(self.driver)
        self.assertEqual(True, self.excepted)