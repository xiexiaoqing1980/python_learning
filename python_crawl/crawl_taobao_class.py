import requests
import time
from selenium import webdriver
import re
import json
import multiprocessing
import xlwt

class CrawlTaobao:
    chromepath = "D:/chromedriver_win32/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    wd = webdriver.Chrome(executable_path=chromepath, chrome_options=chrome_options)  # 打开无痕浏览器
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    cookies_dict = {}
    r = requests.session()
    all_data = []

    def __init__(self,word,pagecount):
        self.word=word
        self.pagecount=pagecount

    def login(self):
        login_url = "https://login.taobao.com/member/login.jhtml?"
        wd=CrawlTaobao.wd
        wd.get(login_url)
        while True:
            if "login.taobao.com" not in wd.current_url:  # == "https://www.taobao.com/":
                break
        time.sleep(1)
        list_cookie = wd.get_cookies()  # get the cookie_dict
        wd.quit()
        for item in list_cookie:
            CrawlTaobao.cookies_dict[item['name']] = item['value']  # 转换cookie

        cookies = requests.utils.cookiejar_from_dict(CrawlTaobao.cookies_dict, cookiejar=None,
                                                     overwrite=True)  # 将字典格式的cookie转换为cookiejar，实现自动维护
        CrawlTaobao.r.cookies = cookies

    def home_page(self):
        t = time.localtime()
        params = {
            "q": self.word,
            'initiative_id': 'staobaoz_%s%02d%02d' % (t[0], t[1], t[2]),
            'Connection': 'close'
        }
        initiative_id = 'staobaoz_%s%02d%02d' % (t[0], t[1], t[2])
        home_page_url = "https://s.taobao.com/search?q={}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306".format(
            self.word)
        # WebDriverWait(wd, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[1]/span/strong")))
        response = CrawlTaobao.r.get(home_page_url, headers=CrawlTaobao.headers, params=params)
        self.parse_response(response.text)

    def next_page(self):
        get_args = {}  # 创建参数字典
        # bcoffset=
        # ntoffset=
        # s=44
        pool = multiprocessing.Pool(multiprocessing.cpu_count())  # 多线程
        for i in range(1, self.pagecount):
            # search_url = "https://s.taobao.com/search?data-key=s&ajax=true&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
            search_url = "https://s.taobao.com/search?data-key=s&ajax=true&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190325&ie=utf8&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48"
            ktsts = time.time()
            get_args['_ksTS'] = "%s_%s" % (int(ktsts * 1000), str(ktsts)[-3:])
            get_args['callback'] = "jsonp%s" % (int(str(ktsts)[-3:]) + 1)
            get_args['q'] = self.word
            get_args['data-value'] = 44 * i
            if i > 1:
                get_args['s'] = 44 * (i - 1)
            response = CrawlTaobao.r.get(search_url, params=get_args)
            html = response.text
            self.parse_response(html)

    def parse_response(self,response):
        content_dict = {}
        if "g_page_config" in response:
            content = re.findall(r'g_page_config =(.*?)g_srp_loadCss', response, re.S)[0]
            content = content.strip()[:-1]  # 去除空格后去除后面的号
            content_dict = json.loads(content)
        elif "jsonp" in response:
            content = re.findall(r'{.*}', response, re.S)[0]
            content_dict = json.loads(content)
        try:
            data_list = content_dict['mods']['itemlist']['data']['auctions']
        except KeyError as E:
            print(E)
        else:
            for item in data_list:
                temp = {
                    'raw_title': item['raw_title'],
                    'view_price': item['view_price'],
                    'view_sales': item['view_sales'] if "view_sales" in item.keys() else "值为空",
                    'view_fee': '否' if float(item['view_fee']) else '是',
                    'isTmall': '是' if item['shopcard']['isTmall'] else '否',
                    'area': item['item_loc'],
                    # 'name': item['nick'],
                    'detail_url': "http:" + item['detail_url'] if item['shopcard']['isTmall'] else item['detail_url'],
                    "comment_count": item["comment_count"] if item["comment_count"] else "无评论数"
                }
                CrawlTaobao.all_data.append(temp)


    def write_into_excel(self,parse_data):
        f = xlwt.Workbook(encoding='utf-8')
        sheet01 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
        # 写标题
        sheet01.write(0, 0, '标题')
        sheet01.write(0, 1, '标价')
        sheet01.write(0, 2, '购买人数')
        sheet01.write(0, 3, '是否包邮')
        sheet01.write(0, 4, '是否天猫')
        sheet01.write(0, 5, '地区')
        # sheet01.write(0, 6, '店名')
        sheet01.write(0, 6, 'url')
        sheet01.write(0, 7, '评论数')

        # write data
        for i in range(len(parse_data)):  # 传入列表
            sheet01.write(i + 1, 0, parse_data[i]['raw_title'])  # 纯文本
            sheet01.write(i + 1, 1, parse_data[i]['view_price'])
            sheet01.write(i + 1, 2, parse_data[i]['view_sales'])
            sheet01.write(i + 1, 3, parse_data[i]['view_fee'])
            sheet01.write(i + 1, 4, parse_data[i]['isTmall'])
            sheet01.write(i + 1, 5, parse_data[i]['area'])
            # sheet01.write(i + 1, 6, parse_data[i]['name'])
            sheet01.write(i + 1, 6, parse_data[i]['detail_url'])
            sheet01.write(i + 1, 7, parse_data[i]['comment_count'])

        f.save(u'D://搜索%s的结果.xls' % self.word)  # 'python

if __name__ == '__main__':
    ct=CrawlTaobao("箱包",2)
    ct.login()
    ct.home_page()
    print(CrawlTaobao.all_data)
    # ct.next_page()
    # ct.write_into_excel(ct.all_data)


