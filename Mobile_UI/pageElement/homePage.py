import comm.common as common
#系统弹窗权限
def click_Allow(driver):
        xpath = ("xpath", "//*[@text='ALLOW']")
        common.window_pop(driver,xpath,1)
#判断主界面是否加载到数据
def is_empty(driver):
    isExist = common.isElementExist(1, driver, 'iv_empty')
    return isExist
#首页加载为空时，点击重新加载
def click_empty(driver):
    driver.find_element_by_id('iv_empty').click()
#点击列表中一首歌进入播放列表页
def click_list(driver):
    driver.find_element_by_id('daily_title').click()
#点击播放按钮
def click_paly(driver):
    driver.find_element_by_id('tv_play').click()
'''
判断是否有系统弹窗
0：text
1: id
2:name
'''
def sys_playPermiss(driver):
    isExist = common.isElementExist(1, driver, 'tv_des')
    return isExist
#点击播放权限框
def click_pop(driver):
    xpath = ("xpath", "//*[@text='OK']")
    common.window_pop(driver,xpath,1)
#打开Music的权限
def open_playPermiss(driver):
    driver.find_element_by_id('switch_widget').click()
#点击手机自带返回键
def click_back(driver):
    driver.keyevent(4)
#点击首页Home菜单
def click_home(driver):
    driver.find_element_by_id('navigation_home').click()
#点击首页Search菜单
def click_search(driver):
    driver.find_element_by_id('navigation_search').click()
#点击搜索框
def click_searchbg(driver):
    driver.find_element_by_id('search_recommend_top_edit_bg').click()
#搜索输入框
def search_input(driver,text):
    driver.find_element_by_id('search_edit').send_keys(text)
#点击youtube进行搜索
def click_youtube(driver):
    driver.find_element_by_id('search_from_youtube_layout').click()
#点击要查找的视频,进行播放
def click_video(driver):
    driver.find_element_by_xpath("//*[@text='Phone Call']").click()
#获取视频上面的分钟数
def get_time(driver):

    strTime = driver.find_element_by_id('tv_total_time').text
    minute=int(strTime.split(':')[0][1])
    second = int(strTime.split(':')[1])
    if minute > 0:
        minute = 60*minute
    if second >= 0:
        second = minute + second
    else:
        second = second[1]
        second = minute + second
    return second-10