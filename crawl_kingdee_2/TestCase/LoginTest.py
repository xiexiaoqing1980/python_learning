
import unittest
import crawl_kingdee_2.loginPage
from  selenium import webdriver

class loginTest(unittest.TestCase):
    """"
     The cases to login
    """
    def setUp(self):
        chromepath = "D:/chromedriver_win32/chromedriver.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver  = webdriver.Chrome(executable_path=chromepath, chrome_options=chrome_options)
        self.base_url="https://ierp.kingdee.com:2024/biz15/index.html"

    def test_input_uername(self):
        login_page=loginPage(self.driver,self.base_url,)
