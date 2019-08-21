from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):
    """
        This is a base page class for Page Object.Package the common methods such as driver, url ,FindElement
        """
    def __init__(self,driver ,base_url):
        self.driver=driver
        self.base_url = base_url

    def find_element(self, *loc):
        """
        The method is used to find the elements in page
        :param loc: BY.XX
        :return: self.driver.find_element(*loc)
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        """
        The method is used to send keys to input fileds
        :param loc: target element
        :param vaule: to be tested values
        :param clear_first:
        :param click_first:
        :return:
        """
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))





