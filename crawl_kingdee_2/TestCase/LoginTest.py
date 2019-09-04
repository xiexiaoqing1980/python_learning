
import unittest
import crawl_kingdee_2.loginPage as loginPage
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

    def login_fail(self):
        self._login("")
        assert()


    def login_success(self):
        login_page=loginPage(self.driver,self.base_url,"金蝶云苍穹")
        login_page.open()
        login_page.input_username("18826135235")
        login_page.input_password("1234567")
        login_page.submit_button()

    def _login(self,username,password):
        login_page = loginPage(self.driver, self.base_url, "金蝶云苍穹")
        login_page.open()
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.submit_button()




