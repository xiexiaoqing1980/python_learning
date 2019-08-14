import requests
import re
import http.cookiejar as cj
import json

# --------------------------------------------只能用于单次登录，一旦登录超时，cookie就会失效---------------------
#URL="https://ierp.kingdee.com:2024/devbos/login.html?redirect=https://ierp.kingdee.com:2024/devbos/"
import json

agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
headers = {
    "HOST": "ierp.kingdee.com:2024",
    "Referer": "https://ierp.kingdee.com:2024/mainbos",
    "User-Agent": agent}


# cookie={ "Hm_lpvt_a96914087b350d1aa86c96cdbf56d5e5":'1539570181',
#         "Hm_lvt_a96914087b350d1aa86c96cdbf56d5e5":"1539570181",
#         'KERPSESSIONID':'54689dd6-f0ad-4158-bd62-7126e869974e',
#         '_jzqa':'1.3537821092574807000.1539570181.1539570181.1539570181.1',
#         '_jzqc':'1',
#         'at':'a0505690-9338-44ed-a634-3104f30790c9',
#         'cd':'yunzhijia.com',
#         'cn':'383cee68-cea3-4818-87ae-24fb46e081b1',
#         'cu':'5a9661d3e4b0b31aea452a0b',
#         'lappKey':'lightapp_1440decd1ab5d03ee13a1dcf5592ed7a',
#         'logintype5a9661d3e4b0b31aea452a0b':'0'
#        }

cookie={
        "KERPSESSIONID":"b4924508-92c8-44fc-97e4-690cd57c387d",
        "uedcms":"s%3AsdtqfmQihSUBYQTRn247bBl_DDEjCH-C.cbSNdfAAm%2FXt8X0VoWqTMjhjDRTOODiaaLWnsOmDQpY"
        }

# ---------写入文件中
# with open("cookies.json",'w+') as f:
#     json.dump(cookie , f)

session = requests.session()
# session.cookies=cj.LWPCookieJar()   # 接入容器
# session.cookies.save(filename='cookies.txt', ignore_discard=True, ignore_expires=True)
# session
session.headers = headers
requests.utils.add_dict_to_cookiejar(session.cookies, cookie) #requests只能保持 cookiejar 类型的cookie，而我们手动构建的cookie是dict类型的。所以要把dict转为 cookiejar类型


# 1、先获取到单元测试下的选项卡：首页、测试报告等,pageId: unitroot355b7c7143fe4321a8b380361507f4ce   params: [{"key":"bizcustomlistap","methodName":"itemClick","args":[{"bizappid":"0a1f79d700004fac"},"listunit"],"postData":[]}]
# 先要获得pageid：


URL1='https://ierp.kingdee.com:2024/mainbos/form/batchInvokeAction.do'
data1={"pageId":"unitrootda47918d532d4c6aad9968dd45fd1156",        #pageid在此处会变化，需要做参数替换
        'params':'[{"key":"bizcustomlistap","methodName":"itemClick","args":[{"bizappid":"0a1f79d700004fac"},"listunit"],"postData":[]}]'
          }
jsondata1=session.post(URL1,data=json.dumps(data1),headers=headers)
jsondata1.encoding="utf-8"
# print(jsondata1.text)



url2="https://ierp.kingdee.com:2024/mainbos/metadata/getDomainModel.do?modelType=BaseFormModel"
jsondata2=session.get(url2)
print(jsondata2.text)

# 2、-------获取单元测试下的首页表单：URL=‘https://ierp.kingdee.com:2024/mainbos/form/batchInvokeAction.do’，pageId: unitroot355b7c7143fe4321a8b380361507f4ce
# params: [{"key":"bizcustomlistap","methodName":"itemClick","args":[{"bizappid":"0a1f79d700004fac","bizunitid":"0a1f79d7000052ac"},"listpage"],"postData":[]}]
# url2 = "https://ierp.kingdee.com:2024/mainbos/form/batchInvokeAction.do"
# data2={
#         "pageId":"unitroot355b7c7143fe4321a8b380361507f4ce", 
#         'params':'[{"key":"bizcustomlistap","methodName":"itemClick","args":[{"bizappid":"0a1f79d700004fac","bizunitid":"0a1f79d7000052ac"},"listpage"],"postData":[]}]'
#         }
#-----------
# with open('cookies.json', 'r') as cookies_file:
#     cookie_json = json.load(cookies_file)
# response=session.get(url)
# response.encoding='utf-8'
# print(response.cookies.get_dict())
# print(response.headers)




#将cookie存入本地---------：
'''#载入本地cookie
s = requests.session()
s.cookies = cj.LWPCookieJar(filename='cookies.txt')
s.cookies.load(filename='cookies.txt', ignore_discard=True)
'''