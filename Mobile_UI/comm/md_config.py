import os
import configparser
#获取config配置文件
#其中os.path.split(os.path.realpath(__file__))是得到当前文件夹目录
path=os.path.split(os.path.dirname(__file__))[0] + '\config.ini'
#实例化configParser对象
config = configparser.ConfigParser()
config.read(path,encoding='utf-8')
#根据标识和key获取相应的键值
def getConfig(section,key):

    value = config.get(section, key)
    return value
#获取数据库配置的相应键值
def getDb(key):
    value = config.get("db", key)
    return value
#获取日志配置的相应键值
def getLog(key):
    value = config.get("log", key)
    return value
#获取浏览器配置的相应键值
def getDriver():
    value = int(config.get("browser", "browserType"))
    return value
#获取测试url
def getUrl():
    value = int(config.get("url", "Environmental"))
    if value == 0:
        value = config.get("url", "testUrl")
    else:value = config.get("url", "formalUrl")
    return value
#运行结果是否保留的参数
def getResult():
    value = int(config.get("result","isClear"))
    return value
#返回邮件服务器
def getServer():
    Smtp_Server = config.get('email','Smtp_Server')
    return Smtp_Server
#邮件发送者邮箱
def getSender():
    Smtp_Sender = config.get('email','Smtp_Sender')
    return Smtp_Sender
#邮件发送者的邮箱密码
def getSender_Pwd():
    Smtp_Sender_Password = config.get('email','Smtp_Sender_Password')
    return Smtp_Sender_Password
#邮件接收者的邮箱
def getReceiver():
    Smtp_Receiver = config.get('email','Smtp_Receiver')
    return Smtp_Receiver
