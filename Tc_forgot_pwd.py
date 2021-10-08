import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class TC_customer_forgotpwd(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ebuy(self):
        homepage = "https://s2-8380.herokuapp.com/"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://s2-8380.herokuapp.com/")
        elem = driver.find_element_by_xpath("/html/body/nav/li/ul[2]/a[1]")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/p/a")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/form/div/div/input")
        elem.send_keys("kavyaravi39@gmail.com")
        elem = driver.find_element_by_xpath("/html/body/div/form/p/input")
        elem.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()


if __name__ == "__main__":
    unittest.main()
