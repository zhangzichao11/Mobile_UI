import os
import time
import unittest
#导入邮件模块
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import comm.md_config as myConfig
from comm.md_logger import myLog
path = os.path.split(os.path.dirname(__file__))[0]
'''
read case name from 'caseList.txt'
:return:caseList
'''
def set_case_list():

    caseList = []
    caseListPath = os.path.join(os.path.split(os.path.dirname(__file__))[0], "caseList.txt")
    fb = open(caseListPath,encoding='UTF-8')
    for case in fb.readlines():
        caseName = str(case)
        if caseName != "" and not caseName.startswith("#"):
            caseList.append(caseName.replace("\n", ""))
    fb.close()
    return caseList

"""
set test suite
return:suite_list
"""
def set_suite():
    global filePath
    suite_list = unittest.TestSuite()
    suite_module = []

    case_list = set_case_list()
    for case in case_list:
        case_Name = str(case)
        filePath = os.path.join(path, 'testCase'+'/')
        discover = unittest.defaultTestLoader.discover(filePath, pattern=case_Name+'.py', top_level_dir=None)
        suite_module.append(discover)

    if len(suite_module) > 0:
        for case in suite_module:
            suite_list.addTest(case)
    else:
        return None
    return suite_list

'''
send email
file_Path:html file path
projectName:project Name
return:True or False
'''
# noinspection PyTypeChecker
def send_Mail(file_Path, projectName):
    f = open(file_Path, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    Smtp_Server = myConfig.getServer()
    try:
        smtp = smtplib.SMTP(Smtp_Server, 25)
        sender = myConfig.getSender()
        password = myConfig.getSender_Pwd()
        receiver = myConfig.getReceiver()
        smtp.login(sender, password)
        msg = MIMEMultipart()
        # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
        # 发送正文
        text = MIMEText(mail_body, 'html', 'utf-8')
        # 定义邮件正文标题
        text['Subject'] = Header(projectName + '自动化测试报告', 'utf-8')
        msg.attach(text)
        # 发送附件
        # Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
        msg['Subject'] = Header('[测试用例执行结果:]'+ projectName + '自动化测试报告' + now, 'utf-8')
        msg_file = MIMEText(mail_body, 'html', 'utf-8')
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file['Content-Disposition'] = 'attachment; filename="{projectName} Report.html"'.format(projectName=projectName)
        msg.attach(msg_file)
        # 定义发件人，如果不写，发件人为空
        msg['From'] = sender
        # 定义收件人，如果不写，收件人为空
        msg['To'] = receiver
        smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
        smtp.quit()
        return True
    except smtplib.SMTPException as e:
        print(str(e))
        return False
