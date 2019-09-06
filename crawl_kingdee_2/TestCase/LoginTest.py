
import unittest
import crawl_kingdee_2.loginPage as loginPage
from  selenium import webdriver
from selenium.webdriver.common.by import By

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

    def login_test1_fail(self):
        self._login("18826135235",'123456')
        assert("用户名或密码错误" in self.driver.page_source)


    def login_test2_success(self):
        self.__login("18826135235", '1234567')
        assert ("")

    def __login(self,username,password):
        login_page = loginPage(self.driver, self.base_url, "金蝶云苍穹")
        login_page.open()
        title=login_page.find_element(*(By.XPATH,'//*[@class="KingdeeCloud_title_3ZXK"]'))
        self.assertIsNotNone(title)
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.click_submit()

if __name__ == '__main__':
     unittest.main()



