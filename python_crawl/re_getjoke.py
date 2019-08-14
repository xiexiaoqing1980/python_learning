import requests
from bs4 import BeautifulSoup 
import re
import time
import multiprocessing

def get_context(url):
    result=requests.get(url)
    result.encoding='utf-8'
    html=result.text
    key_string='<div.*?class="author.*?">.*?<a.*?>.*?</a>.*?<a.*?>.*?<h.*?>(.*?)</h.*?>.*?</a>.*?'+'<div.*?class="articleGender.*?">(.*?)</div>.*?'
    pattern=re.compile(key_string,re.S)
    items=re.findall(pattern,html)  
    return items

def singleprocess():
    result=[]
    start_time=time.time()
        #参数化字符串格式
    for i in range(1,10):
        url='http://www.qiushibaike.com/hot/page/%d'%i 
        items=get_context(url)                    #得到所有是元素为元祖（名称加年龄）的列表：[('\n小色色啊\n', '27')]
    # items=re.search(pattern,html)
    # print(items.group())
        # items.append("第%d页："%i+str(items))
        # result.append(items)
        print("第%d页："%i,items)
    # print(result)
    end_time=time.time()
    print('single  cost %s'%str(end_time-start_time))


def multiprocess_test():
    result=[]
    resultpool=[]
    
    pool=multiprocessing.Pool(multiprocessing.cpu_count())
    start_time=time.time()
    # for i in range(1,7):
    #     url='http://www.qiushibaike.com/hot/page/%d'%i 
        
        # print(items.get())
        # result.append(pool.apply_async(get_context,args=(url,)))
    page_urls=['http://www.qiushibaike.com/hot/page/%d'%i for i in range(1,10)]   #列表
    
    # print(result)
    # pool.close()
    # pool.join()
    # for item in result:
    #     # print(item.get())
    #     resultpool.append(item.get())
    print(pool.map(get_context,page_urls))
    # print(len(result))
    end_time=time.time()
    print('it cost %s'%str(end_time-start_time))



if __name__ == '__main__':
    singleprocess()
    print("---------------------------------")

    multiprocess_test()