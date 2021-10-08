import unittest
import time
from selenium import webdriver


class Tc_checkout(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ebuy(self):
        pwd = "qg"
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
        elem = driver.find_element_by_xpath("/html/body/div[3]/p/a[2]")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[1]/input")
        elem.send_keys("kavya")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[2]/input")
        elem.send_keys("kavya")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[3]/input")
        elem.send_keys("kavyaravi39@gmail.com")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[4]/input")
        elem.send_keys("6823759000")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[5]/input")
        elem.send_keys("4155N 145th Plz")
        time.sleep(3)
        elem = driver.find_element_by_xpath("//html/body/div[3]/form/p[6]/input")
        elem.send_keys("68116")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[7]/input")
        elem.send_keys("Omaha")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[8]/input")
        elem.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()