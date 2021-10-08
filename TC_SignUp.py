import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class TC_customer_signup(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ebuy(self):

        homepage = "https://s2-8380.herokuapp.com/"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://s2-8380.herokuapp.com/")
        elem = driver.find_element_by_xpath("/html/body/nav/li/ul[2]/a[2]")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_name("username")
        elem.send_keys("testcustomer_5")
        time.sleep(3)
        elem = driver.find_element_by_name("email")
        elem.send_keys("test@gmail.com")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/div/input")
        elem.send_keys("user@1234")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[4]/div/input")
        elem.send_keys("user@1234")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
