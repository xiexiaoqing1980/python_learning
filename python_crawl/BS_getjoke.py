import requests
from bs4 import BeautifulSoup 
import re

url='http://www.qiushibaike.com/hot/page/1'
result=requests.get(url)
soup=BeautifulSoup(result.text)
# print(soup.prettify())
# pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
#                          'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
# items = re.findall(pattern,result.text)
# content=soup.find_all('div',class_='content')                #获得所有的div及子标签     
# for item in content:
#     print(item.get_text(strip=True)+"\r\n"+'--------------------------')                             #获得标签内的文本,去掉前后的空格:strip=True但加一个换行

# for item in content:
#     for child in item.children:
#         print(child.string)                                     #直接用获取子节点的方式获得span标签
    
# for item in content:
#     all_span=item.find('span')                               #获得的标签再找一遍就可以获得每个标签下的子子标签
#     print(all_span.text)                               #get_text()/.text可以获得完整的文本，但是用string的时候会出现很多None的情况                           
pattern=re.compile('article block untagged')
articles=soup.find_all('div',class_=pattern)
for article in articles:
    author_info=article.find('div',class_='author clearfix')
    name=author_info.find_all('a')[1].get_text(strip=True)
    pattern_gender=re.compile('articleGender')
    age=article.find('div',class_=pattern_gender)
    content=article.find('div',class_='content').find('span').get_text(strip=True)   #利用get_text(strip=True)去掉空格
    vote=article.find('span',class_='stats-vote').get_text(strip=True)
    img=article.find('div','thumb')
    if img!=None:                                           #通过continue去掉带图片的笑话
        continue
    resultset='作者：'+name+'\r\n年龄:'+age.text +"\r\n内容:"+content+"\r\n投票："+vote+'\r\n'
    print(resultset)




    
