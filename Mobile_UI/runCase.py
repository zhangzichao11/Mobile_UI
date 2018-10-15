import os
from comm.HTMLTestRunner import HTMLTestReport
import comm.runSet as runSet
import comm.md_config as myConfig
import comm.common as common
from comm.md_logger import myLog
path = os.path.split(os.path.dirname(__file__))[0]
if __name__ == '__main__':
      '''运行之前获取config.ini配置里面的result,0表示result文件夹下面的内容每次运行都保存下来，
      1表示只保存最后一次运行的结果'''
      result = myConfig.getResult()
      if result == 1:
            #截图文件的路径
            imPath = os.path.join(path, 'Mobile_Ui','result','image')
            #日志文件的路径
            logPath = os.path.join(path, 'Mobile_Ui','result','logs')
            #测试报告的路径
            reportPath = os.path.join(path, 'Mobile_Ui','result','report')
            common.delFile(imPath)
            common.delFile(logPath)
            common.delFile(reportPath)
      suite = runSet.set_suite()
      #获取report的存放路径
      filePath = myLog().getReportPath()
      fb = open(filePath, 'wb')
      runner = HTMLTestReport(stream=fb, verbosity=2, title='Music UI Test', description='Music TestCase')
      runner.run(suite)
      fb.close()
      myLog.logger().info('测试用例个数 %s', suite.countTestCases())
      #测试邮件发送
      mail = runSet.send_Mail(filePath,'Music UI Test')
      if mail:
            myLog.logger().info('邮件发送成功!')
      else:
            myLog.logger().info('邮件发送失败!')
