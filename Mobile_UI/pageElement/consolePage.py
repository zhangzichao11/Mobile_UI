#后台主界面元素
#左侧的音乐歌单选项
def click_MusicNote(driver):
    driver.find_element_by_xpath('//*[@id="nav_bar"]/li[139]/a').click()
#音乐歌单界面的搜索框
def input_Id(driver, id):
    driver.find_element_by_id('query_name').send_keys(id)
#音乐歌单界面的查询按钮
def click_Query(driver):
    driver.find_element_by_id('query_btn').click()
#音乐歌单界面的导出歌单选项
def export_list(driver):
    driver.find_element_by_id('export').click()
#确认导出按钮
def export_btn(driver):
    driver.find_element_by_id('exportBtn').click()
#导入歌单选项
def import_list(driver,path):
    driver.find_element_by_id('fd').send_keys(path)
#SoloSecurity选项
def click_SoloSecurity(driver):
    driver.find_element_by_xpath('//*[@id="nav_bar"]/li[2]/a').click()
#SoloSecurity选项下面的AdsSdk选项
def click_AdsSdk(driver):
    driver.find_element_by_xpath('//*[@id="demo8"]/li[3]/a').click()
