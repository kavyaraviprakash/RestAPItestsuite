import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from datetime import date, timedelta
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TC_add_to_cart(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ebuy(self):

        pwd = "1234login"
        user = "shiri"
        homepage = "https://s2-8380.herokuapp.com/"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://s2-8380.herokuapp.com/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/nav/li/ul[2]/a[1]")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.click()
        time.sleep(3)
        # elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[1]/a")
        # elem.click()
        # time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]/a")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a[2]")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]")
        elem.click()
        time.sleep(3)



    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()