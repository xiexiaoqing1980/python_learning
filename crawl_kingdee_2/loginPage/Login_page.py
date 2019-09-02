from crawl_kingdee_2.BasePage import BasePage
from selenium.webdriver.common.by import By

class Login_page(BasePage):
    username_loc = (By.XPATH, '//*[@id="login-phone"]')
    password_loc = (By.XPATH, '//*[@id="login-password"]/input')
    submit_button=(By.XPATH,'//*[@id="login-btn"]')

    def open(self):
        self.open_page()


    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.submit_button).click()




