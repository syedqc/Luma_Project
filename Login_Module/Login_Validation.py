import datetime
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class login_secanrios(unittest.TestCase):
    def setUp(self):
        global driver
        cur_time = datetime.datetime.now()
        print(cur_time)
        ch_options = Options()
        ch_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", options=ch_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(By.XPATH, "//body[1]/div[2]/header[1]/div[1]/div[1]/ul[1]/li[2]/a[1]").click()

    def test_login_valid(self):
        driver.find_element(By.NAME, "login[username]").send_keys("syedqc09@gmail.com")
        driver.find_element(By.NAME, "login[password]").send_keys("Tajusyed1!")
        driver.find_element(By.NAME, "send").click()
        cur_title = driver.title
        if cur_title == "Home Page - Magento eCommerce - website to practice selenium | demo website for automation testing | selenium practice sites | selenium demo sites | best website to practice selenium automation | automation practice sites Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites":
            print("Test Pass -With valid credentials")
        else:
            print("Test Fail -Unable to login with valid credentials")

    def test_login_invalid(self):
        driver.find_element(By.NAME, "login[username]").send_keys("syedqc0@gmail.com")
        driver.find_element(By.NAME, "login[password]").send_keys("Tajusyed!")
        driver.find_element(By.NAME, "send").click()
        error_alert = driver.find_element(By.XPATH,
                                          "//div[contains(text(),'The account sign-in was incorrect or your account ')]")
        if error_alert.is_displayed():
            print("Test Pass -Unable to login with invalid credentials")
        else:
            print("Test Fail -Report issue error alert not displaying")

    def test_login_VEWP(self):
        driver.find_element(By.NAME, "login[username]").send_keys("syedqc0@gmail.com")
        driver.find_element(By.NAME, "login[password]").send_keys("")
        driver.find_element(By.NAME, "send").click()
        error_alert = driver.find_element(By.ID, "pass-error")
        if error_alert.is_displayed():
            print("Test Pass -Unable to login with valid user without pwd")
        else:
            print("Test Fail -Report issue error alert not displaying")

    def test_login_IPVE(self):
        driver.find_element(By.NAME, "login[username]").send_keys("")
        driver.find_element(By.NAME, "login[password]").send_keys("Tajusyed1!")
        driver.find_element(By.NAME, "send").click()
        error_alert = driver.find_element(By.ID, "email-error")
        if error_alert.is_displayed():
            print("Test Pass -Unable to login with valid pwd without user")
        else:
            print("Test Fail -Report issue error alert not displaying")


def tearDown(self):
    driver.close()


if __name__ == "__main__":
    unittest.main()
