"""
登陆界面的元素
"""
import comm.common as common
#登录名
def setUserName(driver,userName):
    driver.find_element_by_name('email').send_keys(userName)
#登录密码
def setUserPwd(driver, userPwd):
    driver.find_element_by_name('password').send_keys(userPwd)
#判定是否第一次安装
def is_login(driver):
    isExist = common.isElementExist(1, driver, 'splash_first_btn')
    return isExist
#音乐登录按钮
def click_login(driver):
    driver.find_element_by_id('splash_first_btn').click()
#音乐类型选择
def select_type(driver):
    driver.find_element_by_xpath("//*[@text='Country']").click()
    driver.find_element_by_xpath("//*[@text='Jazz']").click()
#判断音乐类型数据是否拉取到
def is_Type(driver):
    isExist = common.isElementExist(0, driver, '//*[@text="Country"]')
    return isExist
#音乐类型保存按钮
def click_save(driver):
    driver.find_element_by_id('customized_btn').click()
#音乐类型界面的下一步按钮
def click_skip(driver):
    driver.find_element_by_id('customized_skip_txt').click()

