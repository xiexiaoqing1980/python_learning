
import unittest
from  crawl_kingdee_2.loginPage.Login_page import Login_page

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
        self.driver  = webdriver.Chrome(executable_path=chromepath, options=chrome_options)
        self.base_url="https://ierp.kingdee.com:2024/biz15/index.html"
        self.login_page = Login_page(self.driver, self.base_url, "金蝶云苍穹")


    def test_login_fail(self):
        self.login_page.login("18826135235",'123456')
        self.assertEqual("用户名或密码错误",self.login_page.find_element(*(By.XPATH ,'//*[@class="Notification_message_2ZKR"]')).text)

    def test_login_success(self):
        self.login_page.login("18826135235", '1234567')


    # def __login(self,username,password):
    #     self.login_page = loginPage(self.driver, self.base_url, "金蝶云苍穹")
    #     login_page.open()
    #     title=login_page.find_element(*(By.XPATH,'//*[@class="KingdeeCloud_title_3ZXK"]'))
    #     self.assertIsNotNone(title)
    #     login_page.input_username(username)
    #     login_page.input_password(password)
    #     login_page.click_submit()
    # def tearDown(self):
    #     self.login_page.close_page()  #关闭当前页面
    #     print(" Page is closed")


if __name__ == '__main__':
     # suite1=unittest.TestLoader().loadTestsFromTestCase(loginTest["test_login_fail"])
     # suite=unittest.TestSuite([suite1])
     suite=unittest.TestSuite()
     suite.addTest(loginTest("test_login_fail"))
     print("method1")
     unittest.TextTestRunner().run(suite)




