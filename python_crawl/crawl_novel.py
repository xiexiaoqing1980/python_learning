import requests
import multiprocessing
from bs4 import BeautifulSoup 
import time
import re

#获取首页的小说类型
headers = {
    'Connection': 'close',
}

def get_classfications(url):
    result=requests.get(url,headers=headers,verify=False)   #防止sll错误
    requests.adapters.DEFAULT_RETRIES = 5
    result.encoding='utf-8'
    # time.sleep(3)
    html=result.text
    soup=BeautifulSoup(html)
    # key_string='<div.*?class="author.*?">.*?<a.*?>.*?</a>.*?<a.*?>.*?<h.*?>(.*?)</h.*?>.*?</a>.*?'+'<div.*?class="articleGender.*?">(.*?)</div>.*?'

    # pattern=re.compile(key_string,re.S)
    # items=re.findall(pattern,html) 
    novel_type=soup.find("div",class_="nav").find_all("a")   #获取下面的所有节点
    type_list={}
    for item in novel_type:
        href_value=item.get("href")
        text=item.get_text(strip=True)
        type_list[href_value]=text

    print(type_list)


def get_updatednovel(upadetd_Url):
    page=requests.get(upadetd_Url,headers=headers,verify=False)
    requests.adapters.DEFAULT_RETRIES = 5
    page.encoding="utf-8"
    html=page.text
    soup=BeautifulSoup(html)
    pattern=re.compile('index_toplist.*?')
    index_toplist=soup.find_all("div",class_=pattern)
    whole_dict={}
    for index in index_toplist:
        title=index.span.get_text(strip=True)   #获取小说类型的列表，依次遍历
        # print(title)
        # topbooks=index.find("div",attrs={"class":pattern,"id":"con_o1g_1"}).find_all("a")
        topbooks=index.find("div",class_="topbooks").find_all("a")
        book_dict={}
        for books in topbooks:
            book_href=books.get("href")
            book_title=books.get("title")
            book_dict[book_href]=book_title
        # whole_list.append(book_list)
            whole_dict[title]=book_dict     #获取所有的字典,缩进不缩进的效果都是一样的
    return whole_dict


def get_context(url):                                 #先试着爬取一篇小说，例如盖世帝尊
    page=requests.get(url,headers=headers,verify=False)
    requests.adapters.DEFAULT_RETRIES = 5
    page.encoding="utf-8"
    soup=BeautifulSoup(page.text)
    # first_chapter=soup.find("a",text=(re.compile("第(1|一)章")))   #找到第一章标签及所有子标签
    dts=soup.find("div",{"id":"list"}).find_all("dt")   #获取所有的dt表格
    chapters={}
    for dt in dts:
        sibling_list=[]
        for sibling in dt.next_siblings:
            if sibling in dts:
                break
            sibling_list.append(sibling)
        chapters[dt.get_text(strip=True)]=sibling_list         #获取两个标签之间的内容
    return chapters
        
        
    # print(chapters)
    # chapter_dict={}
    # for chapter in chapters:
    #     if("<dt>" in chapter):
    #         continue
    #     chapter_url=chapter.a.get("href")
    #     chapter_title=chapter.get_text()
    #     chapter_dict[chapter_url]=chapter_title
    # return chapter_dict
    

    
        



    
    

    
    

    #使用
    # return items



if __name__ == '__main__':
        
        # url="https://www.dingdiann.com"+"ddk_{}/".format(i)
    homepage_url="https://www.dingdiann.com"
    upadetd_Url=homepage_url+"/quanben.html"   #完本小说的链接
    # get_classfications(homepage_url)
    print(get_updatednovel(upadetd_Url))
    # print(get_context(homepage_url+"/ddk297/"))
        






