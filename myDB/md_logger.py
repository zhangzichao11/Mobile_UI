import logging.config
import md_config
import os
import time
from logging.handlers import RotatingFileHandler
#日志内容的格式
format1 = md_config.getConfigLog("format").replace('@', '%')
#日志大小和数目
backupcount = int(md_config.getConfigLog("backupcount"))
maxbytes=int(md_config.getConfigLog("maxbytes"))
#日志级别
level=int(md_config.getConfigLog("level"))
#保存日志到文件的函数
def logger():
    #创建一个logger,并设置级别
    logger1 = logging.getLogger()
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    logpath=os.getcwd() + '/logs/' + rq + '.log'
    #创建一个handler,用于写入文件
    Rthandler = RotatingFileHandler(logpath, maxBytes=maxbytes, backupCount=backupcount, encoding='utf-8')
    # 这里来设置日志的级别
    # CRITICAl    50
    # ERROR    40
    # WARNING    30
    # INFO    20
    # DEBUG    10
    # NOSET    0
    Rthandler.setLevel(level)
    #定义handler的输出格式
    formater = logging.Formatter(format1)
    #给handler添加formatter
    Rthandler.setFormatter(formater)
    #给logger添加handler
    logger1.addHandler(Rthandler)
    return logger1