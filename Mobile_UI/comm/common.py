"""
该类主要是存放一些公共方法，比如：元素查找、截屏
、操作Excel等等
"""
#导入日志模块
from comm.md_logger import myLog

#导入截图模
from PIL import ImageGrab
#读excel模块
import xlrd
import time,os
import shutil
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
filePath:current path
qr：file name format
'''
filePath = os.path.split(os.path.dirname(__file__))[0]
'''
find element
flag:True or Flase
xpath:element xpath
0：text
1: id
2: name
'''
def isElementExist(flag,driver,xpath):
    isExist = True
    if flag == 0:
        # noinspection PyBroadException
        try:
            driver.find_element_by_xpath(xpath).is_displayed()
        except Exception as e:
            myLog.logger().error("查找的元素不存在 %s %s",xpath,e)
            isExist = False
        return isExist
    elif flag == 1:
        # noinspection PyBroadException
        try:
            driver.find_element_by_id(xpath).is_displayed()
        except Exception as e:
            myLog.logger().error("查找的元素不存在 %s %s", xpath, e)
            isExist = False
        return isExist
    elif flag == 2:
        try:
            driver.find_elements_by_name(xpath).is_displayed()
        except Exception as e:
            myLog.logger().error("查找的元素不存在 %s %s", xpath, e)
            isExist = False
        return isExist
'''
Screenshot function
imPath:picture save path
imType: picture type
'''
def Screenshot(imPath,imType):
    im = ImageGrab.grab()
    im.save(imPath, imType)

def Screenshot1():
    rq = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    # log文件的存放路径
    imPath = filePath + '/result/image/' + rq + '.png'
    im = ImageGrab.grab()
    im.save(imPath)
def Screenshot2(imPath):
    im = ImageGrab.grab()
    im.save(imPath)
'''
Delete folder content
path: folder path
'''
def delFile(path):
    shutil.rmtree(path)
    os.makedirs(path)
'''
excel_name:excel file name
sheet_name:sheet name
return:sheet value
'''
def get_excel_value(sheet_name):
    cls = []
    excel_path = filePath + '/data/testCase.xls'
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_Name':
            cls.append(sheet.row_values(i))
    return cls
#Screen swipe
#get Screen size
def getScreenSize(driver):

    size = driver.get_window_size()
    #get width
    width = size['width']
    #get height
    height = size['height']
    return width,height
#swipe up Screen
def swipeUp(driver,n):
    W_size = getScreenSize(driver)
    x1 = int(W_size[0]*0.5)
    y1 = int(W_size[1]*0.75)
    y2 = int(W_size[1]*0.25)
    for i in range(n):
        myLog.logger().info('滑动次数' + str(i+1))
        driver.swipe(x1, y1, x1, y2)
#swipe down Screen
def swipeDown(driver,n):
    W_size = getScreenSize(driver)
    x1 = int(W_size[0] * 0.5)
    y1 = int(W_size[1] * 0.25)
    y2 = int(W_size[1] * 0.9)
    time.sleep(2)
    for i in range(n):
        time.sleep(2)
        driver.swipe(x1, y1, x1, y2)
#swipe left Screen
def swipeLeft(driver,n):
    W_size = getScreenSize(driver)
    x1 = int(W_size[0] * 0.8)
    x2 = int(W_size[0] * 0.2)
    y1 = int(W_size[1] * 0.5)
    time.sleep(2)
    for i in range(n):
        time.sleep(2)
        driver.swipe(x1, y1, x2, y1)
#swipe right Screen
def swipeRight(driver,n):
    W_size = getScreenSize(driver)
    x1 = W_size[0] * 0.2
    x2 = W_size[1] * 0.8
    y1 = W_size[1] * 0.5
    time.sleep(2)
    for i in range(n):
        time.sleep(2)
        driver.swipe(x1, y1, x2, y1)
'''system window pop
    n：search times
'''
def window_pop(driver,xpath,n):

    for i in range(n):
        try:
            em = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(xpath))
            em.click()
            myLog.logger().info('定位成功 %s', em)
        except Exception as e:
            myLog.logger().error('定位播放pop权限框失败 %s', e)