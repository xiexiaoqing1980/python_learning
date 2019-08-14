import requests
from bs4 import BeautifulSoup 
import re

url="http://www.baidu.com"
result=requests.session().get(url)
result.encoding='utf-8'
html=result.text
#--------创建对象
soup=BeautifulSoup(html)
# print(soup.prettify())       #按格式输出

# ------------获取整个标签:tag------------
#print(soup.title)           <title>#########</title> 利用 soup 加标签名轻松地获取这些标签的内容,查找的是在所有内容中的第一个符合要求的标签
#print(soup.name)               获取标签的名称：document
# print(soup.title.name)          获取标签的名称：title
# print(soup.p['id'])            获取标签内属性的属性值

# ----------获得标签内部的文字:NavigableString-----
# print(soup.title.string)       .string:百度一下，你就知道

# --------------beautifulSoup :对象表示的是一个文档的全部内容
# print(soup.attrs)            {}

# ----------Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，

# ------------遍历文档树,直接子节点：.content属性：可以将tag的子节点以列表的方式输出-----------
# print(soup.head.contents)   :     [<meta content="text/html;charset=utf-8" http-equiv="content-type"/>, <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>, <meta content="always" name="referrer"/>, <link href="http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css"/>, <title>百度一下，你就知道</title>]
# print(soup.head.contents[0])       以索引获取元素

# --------.children：它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
# print(soup.head.children)            <list_iterator object at 0x000000D02C409048>
# for i in soup.head.children:         遍历
    # print(i)

# ------.descendants:所有子孙节点,需要遍历
# print(soup.body.descendants)         <generator object descendants at 0x000000AD58A70728>
# for i in soup.body.descendants:
    # print(i)   

# -------.strings获取多个内容，不过需要遍历获取
# for i in soup.body.strings:                    可以任意选择哪个标签下的所有内容
    # print(i)
# ------------ .stripped_strings 可以去除多余空白内容
# for i in soup.body.stripped_strings:                    #可以任意选择哪个标签下的所有内容
    # print(i)


# ------兄弟节点:知识点：.next_sibling .previous_sibling 属性
# print(soup.title.previous_sibling)

#-------全部兄弟节点:知识点：.next_siblings .previous_siblings 属性

# -------前后节点知识点：.next_element .previous_element 属性

# ---所有前后节点知识点：.next_elements .previous_elements 属性



# tag=soup.title.get_text()   直接获取标签内的文本
# print(tag)



# x.get('href')  获取属性值


#-------------------------------- BeautifulSoup中的next_siblings（）很擅长处理带标题行的表格：

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("https://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, "html.parser")
 
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)
