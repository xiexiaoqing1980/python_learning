import requests
import re
import http.cookiejar as cj
#URL="https://ierp.kingdee.com:2024/devbos/login.html?redirect=https://ierp.kingdee.com:2024/devbos/"
import json

agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
headers = {
    "HOST": "www.zhihu.com",
    "Referer": "http://www.zhihu.com",
    "User-Agent": agent}


cookie={ '_xsrf':"7ab1e1be-652d-4716-94a5-ef532edc5975",
        '_zap':"5761664a-58bb-4707-bda1-e1a08c27e466",
        "capsion_ticket":'"2|1:0|10:1539259927|14:capsion_ticket|44:MzUwNDg0NTU0NzFlNDlkZmEzODRmNDdkMmIzYzBlMTE=|b5c38da3549e3ddd46a1bdbcdbdc2f34ac75ac3db6e1fc33523c10089e104354"',
         'd_c0':'"AGCnJ83NWA6PTtFH9DbMJE-xRMZVMwBaWC8=|1539257698"',
         "tgw_l7_route":"170010e948f1b2a2d4c7f3737c85e98c",
         "z_c0":'"2|1:0|10:1539259950|4:z_c0|92:Mi4xOUI4MkFnQUFBQUFBWUtjbnpjMVlEaVlBQUFCZ0FsVk5Mb3lzWEFBUXMtaUhvdElRZ2hfVHlaNFdpWVYwZ1dERWxR|3ab31c043f1672abba84651b5e1bcefb7f786e8b50042c771bb7448dd8066df0"'
 }

# ---------写入文件中
with open("cookies.json",'w+') as f:
    json.dump(cookie , f)

session = requests.session()
# session.cookies=cj.LWPCookieJar()   # 接入容器
# session.cookies.save(filename='cookies.txt', ignore_discard=True, ignore_expires=True)
# session
session.headers = headers
url = "https://www.zhihu.com/question/20502368/answer/15490485"
# requests.utils.add_dict_to_cookiejar(session.cookies, cookies)
#-----------
with open('cookies.json', 'r') as cookies_file:
    cookie_json = json.load(cookies_file)
response=session.get(url, cookies=cookie_json)

print(response)



#将cookie存入本地---------：
'''#载入本地cookie
s = requests.session()
s.cookies = cj.LWPCookieJar(filename='cookies.txt')
s.cookies.load(filename='cookies.txt', ignore_discard=True)
'''