"""
登陆界面的case,登录数据来自于excel
根据用例名来区分进行不同情况的验证，并获取实际验证结果和excel里面的
预期结果进行对比
继承Driver类,获取浏览器的driver
作者:zhangzichao
"""
import time
#导入浏览器driver类
from comm.webDriver import webDriver
#导入界面元素类
import pageElement.loginPage as login_Page
#导入主界面元素
import pageElement.homePage as home_Page
#导入日志模块类
from comm.md_logger import myLog
#导入公共方法类
import comm.common as common
import unittest
import paramunittest
loginCase = common.get_excel_value('login')
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
        #判断是否第一次登录,如果是走第一次登录的界面,否则走登录后的界面
        if login_Page.is_login(self.driver):

            #开始按钮
            login_Page.click_login(self.driver)
            time.sleep(2)
            #点击开始按钮后进行截屏
            common.Screenshot1(self.driver)
            #判定是否拉取到音乐类型的后台数据,如果拉取到就进行选择,否则直接点击下一步
            if login_Page.is_Type(self.driver):
                # 音乐类型选择
                login_Page.select_type(self.driver)
                #音乐类型保存
                login_Page.click_save(self.driver)
                time.sleep(5)
                #系统权限框
                home_Page.click_Allow(self.driver)
                time.sleep(3)
            else:
                login_Page.click_skip(self.driver)
                time.sleep(3)
                #系统权限框
                home_Page.click_Allow(self.driver)
                time.sleep(8)
            if home_Page.is_empty(self.driver):
                home_Page.click_empty(self.driver)
                time.sleep(5)
        #向上滑动,n:滑动次数
        common.swipeUp(self.driver,1)
        #滑动首页后进行截屏
        common.Screenshot1(self.driver)
        #首页点击进入播放列表页
        time.sleep(2)
        home_Page.click_list(self.driver)
        #点击play播放按钮
        home_Page.click_paly(self.driver)
        #判断是否有系统权限弹窗
        if home_Page.sys_playPermiss(self.driver):

            #播放权限框
            home_Page.click_pop(self.driver)
            #播放系统权限界面的截屏
            common.Screenshot1(self.driver)
            #打开music的权限框
            home_Page.open_playPermiss(self.driver)
            # 点击手机返回键,返回程序播放界面
            home_Page.click_back(self.driver)
        # 点击手机返回键,返回程序主界面
        time.sleep(1)
        home_Page.click_back(self.driver)
        time.sleep(2)
        #返回主界面的截屏
        common.Screenshot1(self.driver)
        self.assertEqual(True, self.excepted)

        #正常登陆的测试用例
        '''if self._testMethodDoc == 'test_login1':
            time.sleep(5)
            isLogin = login_Page.isLogin(self.driver)
            try:
                myLog.logger().info("实际结果的值是:%s", isLogin)
                myLog.logger().info("预期结果的值是:%s", self.excepted)
                self.assertEqual(isLogin, self.excepted)
                #登陆成功之后进行截屏
                common.Screenshot1()
                myLog.logger().info("info登录成功....%s", isLogin)
                login_Page.click_exit(self.driver)
            except Exception as e:
                #登陆失败之后进行截屏
                common.Screenshot1()
                myLog.logger().info("登录失败....%s", e)
        #对用户名错误,密码正确的case
        elif self._testMethodDoc == 'test_login2':
            time.sleep(2)
            common.Screenshot1()
            #获取实际的结果值
            act_text = login_Page.userName_Error(self.driver)
            myLog.logger().info("实际结果的值是:%s", act_text)
            myLog.logger().info("预期结果的值是:%s", self.excepted)
            #和预期的结果值进行对比
            self.assertEqual(act_text, self.excepted)
        #对用户名正确,密码错误的case
        elif self._testMethodDoc == 'test_login3':
            time.sleep(2)
            common.Screenshot1()
            #获取实际结果值
            act_text = login_Page.userName_Error(self.driver)
            myLog.logger().info("实际结果的值是:%s", act_text)
            myLog.logger().info("预期结果的值是:%s", self.excepted)
            # 和预期的结果值进行对比
            self.assertEqual(act_text, self.excepted)'''
