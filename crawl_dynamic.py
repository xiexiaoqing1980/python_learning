import requests


#-----------------切换页面动态获取查询编码----

# --------原来的URL-----
# url="http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback38367&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=2&pageHelp.pageSize=25&pageHelp.pageNo=1&pageHelp.endPage=11&_=1540177324195"
url='http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=600035'
# Cookie = "PHPStat_First_Time_10000011=1480428327337; PHPStat_Cookie_Global_User_Id=_ck16112922052713449617789740328; PHPStat_Return_Time_10000011=1480428327337; PHPStat_Main_Website_10000011=_ck16112922052713449617789740328%7C10000011%7C%7C%7C; VISITED_COMPANY_CODE=%5B%22600064%22%5D; VISITED_STOCK_CODE=%5B%22600064%22%5D; seecookie=%5B600064%5D%3A%u5357%u4EAC%u9AD8%u79D1; _trs_uv=ke6m_532_iw3ksw7h; VISITED_MENU=%5B%228451%22%2C%229055%22%2C%229062%22%2C%229729%22%2C%228528%22%5D"
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    # 'Cookie': Cookie,
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    #------原来的host,referer
    # 'Host': 'query.sse.com.cn',
    'Referer':'http://www.sse.com.cn/assortment/stock/list/share/',
    'Host':'www.sse.com.cn'
}

result=requests.get(url,headers=headers)
result.encoding=('utf-8')
print(result.text)