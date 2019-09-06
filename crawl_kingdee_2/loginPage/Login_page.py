from crawl_kingdee_2.BasePage import BasePage
from selenium.webdriver.common.by import By

class Login_page(BasePage):
    username_loc = (By.XPATH, '//*[@placeholder="用户名/手机号/邮箱"]')
    password_loc = (By.XPATH, '//*[@placeholder="登录密码')
    submit_button=(By.XPATH,'//*[@class="Button_button_2R-q"]')

    def open(self):
        self.open_page()

    def input_username(self,username):
        # self.find_element(*self.username_loc).send_keys(username)
        use_element=self.find_element(*self.username_loc)
        self.send_keys(use_element,username)

    def input_password(self,password):
        password_element=self.find_element(*self.password_loc)
        self.send_keys(password_element,password)

    def click_submit(self):
        self.find_element(*self.submit_button).click()






