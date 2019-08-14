from selenium import webdriver
import time
import requests
import re
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromepath="D:/chromedriver_win32/chromedriver.exe"
wd = webdriver.Chrome(executable_path=chromepath)
loginurl="https://ierp.kingdee.com:2024/devbos/login.html?redirect=https://ierp.kingdee.com:2024/devbos/"
# loginurl="https://www.toutiao.com/stream/widget/local_weather/data/?city=%E5%8C%97%E4%BA%AC"
wd.get(loginurl)
wd.find_element_by_xpath('//*[@id="login-phone"]').send_keys("18826135235")
wd.find_element_by_xpath('//*[@id="login-password"]/input').send_keys('1234567')
# verifycode=input("验证码： ")
# wd.find_element_by_xpath('//*[@id="graphicCode"]').send_keys(verifycode)
wd.find_element_by_xpath('//*[@id="login-btn"]').click()
wd.implicitly_wait(15)

# js = "var q=document.getElementsByClassName('oym9trU1 kd-active')"
element=wd.find_element_by_xpath('//*[@class="oym9trU1 kd-hover"]')
wd.execute_script("arguments[0].click();", element)

# wd.implicitly_wait(10)
# time.sleep(50)
#---------------载入cookies--------
# cookies=wd.get_cookies()
# req=requests.Session()
# c=requests.cookies.RequestsCookieJar()
# for cookie in cookies:
#     c.set(cookie['name'],cookie['value'])
#     # req.cookies.set(cookie['name'],cookie['value'])
# req.headers.clear()                                                      # 删除原始req里面标记有python机器人的信息
# req.cookies.update(c)
# print(c)

#-----获取当前窗口句柄---用于页面跳转
now_handle = wd.current_window_handle
print(now_handle)

WebDriverWait(wd, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@title="开发平台"]')))
element1=wd.find_element_by_xpath('//*[@title="开发平台"]')
wd.execute_script("arguments[0].click();", element1)
time.sleep(5)
all_handles=wd.window_handles

# wd.switch_to_window(all_handles[1])
# print(wd.current_window_handle)
for handle in wd.window_handles:
    if handle!=now_handle:
        wd.switch_to_window(handle)
print(wd.current_window_handle)

# ------进入开发服务云------
# WebDriverWait(wd, 60).until(EC.presence_of_element_located((By.XPATH,'//*[@class="kdfont kdfont-guanbiyulan kd-hover-color _1ltLb1eh"]')))
# element4=wd.find_element_by_xpath('//*[@class="kdfont kdfont-guanbiyulan kd-hover-color _1ltLb1eh"]')
# wd.execute_script("arguments[0].click();", element4)

# print(element4)
# WebDriverWait(wd, 60).until(EC.presence_of_element_located((By.XPATH,'//*[@title="开发服务云"]')))
# element3=wd.find_element_by_xpath('//*[@title="开发服务云"]')
# wd.execute_script("arguments[0].click();", element3)
time.sleep(40)
# html = current_window_handle
# print(html)


# application=wd.find_element_by_xpath("//*[@id='']")点击应用

#--------------获取pageid------
# pattern=re.compile(r'.*?<div id="(.+?)".*?data-form-id="pc_main_console"')
# pageid=re.findall(pattern,wd.page_source)
# print(pageid)