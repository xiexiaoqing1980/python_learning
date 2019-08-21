from crawl_kingdee_2.BasePage import BasePage
from selenium.webdriver.common.by import By

class Login_page(BasePage):
    username_loc = (By.XPATH, 'email')
    password_loc = (By.NAME, 'password')
