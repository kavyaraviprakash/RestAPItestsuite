import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class TC_customer_login(unittest.TestCase):
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
        WebDriverWait(driver, 3).until(
            ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-number']")))
        WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable((By.XPATH, "//input[@class='number' and @id='credit-card-number']"))).send_keys(
            "4111 1111 1111 1111")
        driver.switch_to.parent_frame()
        WebDriverWait(driver, 3).until(
            ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-cvv']")))
        WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable((By.XPATH, "//input[@class='cvv' and @id='cvv']"))).send_keys("123")
        driver.switch_to.parent_frame()
        WebDriverWait(driver, 3).until(ec.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//iframe[@id='braintree-hosted-field-expirationDate']")))
        WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable((By.XPATH, "//input[@class='expirationDate' and @id='expiration']"))).send_keys(
            "12/28")
        driver.switch_to.parent_frame()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='payment']/input[3]").click()
        time.sleep(15)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
