from selenium import webdriver
import time
import requests
import re
from bs4 import BeautifulSoup as BS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def getelement_by_xpath(path):
    WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.XPATH,path)))
    element=wd.find_element_by_xpath(path)
    return element

def authorize():
    wd.get(loginurl)
    try:
        getelement_by_xpath('//*[@id="login-phone"]').send_keys("administrator")
        getelement_by_xpath('//*[@id="login-password"]/input').send_keys('1234567')
    except Exception as error:
        wd.quit()
    else:
        pass
    getelement_by_xpath('//*[@id="login-btn"]').click()
    application=getelement_by_xpath('//*[@class="oym9trU1 kd-hover"]')
    wd.execute_script("arguments[0].click();",application)
    service=getelement_by_xpath('//*[@title="基础服务"]')
    wd.execute_script("arguments[0].click();",service)
    user=getelement_by_xpath('//*[@title="全功能用户"]')
    wd.execute_script("arguments[0].click();",user)
    add_user=getelement_by_xpath('//*[@title="添加用户"]')
    wd.execute_script("arguments[0].click();",add_user)

    getelement_by_xpath('//*[@class="_1vTTLSCX _3MN-_9A6 _2wCutmnQ _3csOpDHD"]').send_keys("谢敬青")
    select_name=getelement_by_xpath('//li[@class="_17YKqErs select-selected"]')
    wd.execute_script("arguments[0].click();",select_name)

    save_name=getelement_by_xpath('//*[@id="btnsave"]')
    wd.execute_script("arguments[0].click();",save_name)
    wd.close()

def login():
    wd.get(loginurl)
    getelement_by_xpath('//*[@id="login-phone"]').send_keys("18826135235")
    getelement_by_xpath('//*[@id="login-password"]/input').send_keys('1234567')
    # verifycode=input("验证码： ")
    # wd.find_element_by_xpath('//*[@id="graphicCode"]').send_keys(verifycode)
    # wd.implicitly_wait(5)
    # wd.find_element_by_xpath('//*[@id="login-btn"]').click()
    getelement_by_xpath('//*[@id="login-btn"]').click()
    wd.implicitly_wait(5)
    try:
        element=wd.find_element_by_xpath('//*[@class="oym9trU1 kd-hover"]')
        wd.execute_script("arguments[0].click();", element)
    except Exception as error:
        print(error)
        # wd.quit()
    else:
        pass
    # wd.implicitly_wait(20)
    # js = "var q=document.getElementsByClassName('oym9trU1 kd-active')"

    now_handle = wd.current_window_handle 
    # print(now_handle)
    #-----获取当前窗口句柄---用于页面跳转
    path='//*[@title="开发平台"]'
    WebDriverWait(wd, 30).until(EC.presence_of_element_located((By.XPATH,path)))
    element1=wd.find_element_by_xpath(path)
    wd.execute_script("arguments[0].click();", element1)
    time.sleep(5)

    all_handles=wd.window_handles
    wd.switch_to_window(all_handles[-1])

    # ------叉掉弹出框----
    WebDriverWait(wd, 30).until(EC.presence_of_element_located((By.XPATH,'//i[@class="kdfont kdfont-guanbiyulan kd-hover-color _1ltLb1eh"]')))
    element1=wd.find_element_by_xpath('//*[@class="kdfont kdfont-guanbiyulan kd-hover-color _1ltLb1eh"]')
    wd.execute_script("arguments[0].click();", element1)


    # ---------进入开发演示云------
    WebDriverWait(wd, 60).until(EC.presence_of_element_located((By.XPATH,'//*[@title="开发演示云"]')))
    element3=wd.find_element_by_xpath('//*[@title="开发演示云"]')
    wd.execute_script("arguments[0].click();", element3)

if __name__ == '__main__':
    
    # wd.find_element_by_xpath('//*[@id="login-phone"]').send_keys("18826135235")
    # wd.find_element_by_xpath('//*[@id="login-password"]/input').send_keys('1234567')

    #----先进行授权--------
    
    

    #--------正式登陆--------
    chromepath="D:/chromedriver_win32/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    wd = webdriver.Chrome(executable_path=chromepath ,chrome_options=chrome_options)      #打开无痕浏览器
    loginurl="https://ierp.kingdee.com:2024/devbos/login.html?redirect=https://ierp.kingdee.com:2024/devbos/"
    authorize()
    # login()

