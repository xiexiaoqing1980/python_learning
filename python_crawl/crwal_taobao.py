import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import json

'''
need to login first to get 
'''
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


def login():
    login_url = "https://login.taobao.com/member/login.jhtml?"
    wd.get(login_url)
    while True:
        if wd.current_url == "https://www.taobao.com/":
            break
    time.sleep(1)
    list_cookie = wd.get_cookies()  # get the cookie_dict
    wd.quit()
    for item in list_cookie:
        cookies_dict[item['name']] = item['value']  # 转换cookie

    cookies = requests.utils.cookiejar_from_dict(cookies_dict, cookiejar=None,
                                                 overwrite=True)  # 将字典格式的cookie转换为cookiejar，实现自动维护
    r.cookies = cookies


def home_page(word):
    # WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#J_Quick2Static")))
    # switch_button=wd.find_element_by_css_selector("#J_Quick2Static")
    # wd.execute_script("arguments[0].click();", switch_button)
    #
    # WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#TPL_username_1")))
    # wd.find_element_by_css_selector("#TPL_username_1").send_keys("18826135235")
    #
    # WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#TPL_password_1")))
    # wd.find_element_by_css_selector("#TPL_username_1").send_keys("")
    t = time.localtime()
    params = {
        "q": word,
        'initiative_id': 'staobaoz_%s%02d%02d' % (t[0], t[1], t[2]),
        'Connection': 'close'
    }
    initiative_id = 'staobaoz_%s%02d%02d' % (t[0], t[1], t[2])
    home_page_url = "https://s.taobao.com/search?q={}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306".format(word)
    # WebDriverWait(wd, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[1]/span/strong")))

    response = r.get(home_page_url, headers=headers, params=params)
    parse_response(response.text)
    # print(response.text)
    # print(cookies)
    # print(response.cookies.get_dict())


def next_page(word, pagecount):
    get_args = {}  # 创建参数字典
    # bcoffset=
    # ntoffset=
    # s=44
    for i in range(1, pagecount):
        # search_url = "https://s.taobao.com/search?data-key=s&ajax=true&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
        search_url = "https://s.taobao.com/search?data-key=s&ajax=true&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190325&ie=utf8&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48"
        ktsts = time.time()
        get_args['_ksTS'] = "%s_%s" % (int(ktsts * 1000), str(ktsts)[-3:])
        get_args['callback'] = "jsonp%s" % (int(str(ktsts)[-3:]) + 1)
        get_args['q'] = word
        get_args['data-value'] = 44 * i
        if i > 1:
            get_args['s'] = 44 * (i - 1)
        response = r.get(search_url, params=get_args)
        html = response.text
        with open("D:/result_response.txt", "a+") as f:
            f.write(html + "\r\n")
        time.sleep(2)
        parse_response(html)


def parse_response(response):
    content_dict = {}
    if "g_page_config" in response:
        content = re.findall(r'g_page_config =(.*?)g_srp_loadCss', response, re.S)[0]
        content = content.strip()[:-1]  # 去除空格后去除后面的号
        content_dict = json.loads(content)
    elif "jsonp" in response:
        content = re.findall(r'{.*}', response, re.S)[0]
        content_dict = json.loads(content)
    data_list = content_dict['mods']['itemlist']['data']['auctions']
    for item in data_list:
        temp = {
            'title': item['title'],
            'view_price': item['view_price'],
            # 'view_sales': item['view_sales'],
            'view_fee': '否' if float(item['view_fee']) else '是',
            'isTmall': '是' if item['shopcard']['isTmall'] else '否',
            'area': item['item_loc'],
            'name': item['nick'],
            'detail_url': item['detail_url'],
        }
        all_data.append(temp)


if __name__ == '__main__':
    # print("测试{}".fo
    login()

    home_page("箱包")

    next_page("箱包", 100)
    with open("D:/result.txt","w+") as f:
        f.write(str(all_data)+"\r\n")
    print(all_data)
    print(len(all_data))

    # next_page("箱包")

    # response=requests.get("https://s.taobao.com/search?data-key=s&data-value=44&ajax=true&_ksTS=1553436611363_937&callback=jsonp938&q=%E7%AE%B1%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48",headers=headers)
    # print(response.text)



