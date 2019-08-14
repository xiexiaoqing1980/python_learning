#-*-coding:utf-8-*-
#中文编码的问题
import requests
import selenium
from bs4 import BeautifulSoup
import sys


url="https://www.toutiao.com/"
agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
headers = {
    "HOST": "www.zhihu.com",
    # "Referer": "http://www.zhihu.com",
    "User-Agent": agent}


# session_request=requests.session()
# result=session_request.post(url,data=post_data)
result=requests.get(url,headers=headers)
#print(result.encoding)  #
#print(result.apparent_encoding)
result.encoding=('utf-8')
print(result.text)

# page=session_request.get('http://172.18.5.32:8080/ierp/index.html#/dform?formId=pc_main_console')
# page.encoding=('utf-8')
# print(page.text)
