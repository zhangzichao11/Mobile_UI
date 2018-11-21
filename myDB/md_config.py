import os
import configparser
#获取config配置文件
#其中os.path.split(os.path.realpath(__file__))是得到当前文件夹目录
path=os.path.split(os.path.realpath(__file__))[0] + '/config.ini'
#实例化configParser对象
config = configparser.ConfigParser()
print("路径是:",path)
config.read(path)
#根据标识和key获取相应的键值
def getConfig(section,key):

    value = config.get(section, key)
    return value
#获取数据库配置的相应键值
def getConfigDb(key):
    value = config.get("db", key)
    return value
#获取日志配置的相应键值
def getConfigLog(key):
    value = config.get("log", key)
    return value