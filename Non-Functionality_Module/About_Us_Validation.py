import datetime
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Aboutus_secanrios(unittest.TestCase):
    def setUp(self):
        global driver
        cur_time = datetime.datetime.now()
        print(cur_time)
        ch_options = Options()
        ch_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", options=ch_options)
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(By.XPATH, "//body[1]/div[2]/header[1]/div[1]/div[1]/ul[1]/li[2]/a[1]").click()
        driver.find_element(By.NAME, "login[username]").send_keys("syedqc09@gmail.com")
        driver.find_element(By.NAME, "login[password]").send_keys("Tajusyed1!")
        driver.find_element(By.NAME, "send").click()
        cur_title = driver.title
        if cur_title == "Home Page - Magento eCommerce - website to practice selenium | demo website for automation testing | selenium practice sites | selenium demo sites | best website to practice selenium automation | automation practice sites Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites":
            print("Test Pass -Logged with valid credentials")
        else:
            print("Test Fail -Unable to login with valid credentials")

    def test_aboutus_valid(self):
        driver.find_element(By.XPATH, "//a[contains(text(),'About us')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'SoftwareTestingBoard.com')]").click()
        assert driver.title == "Welcome to Software Testing Board - Software Testing Board"
        driver.back()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(text(),'https://softwaretestingboard.com/blogs/')]").click()
        assert driver.title == "STB Blogs - Quality in mind? Press it here."
        driver.back()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(text(),'https://softwaretestingboard.com/write-for-us/')]")
        assert driver.title == "About us Magento Commerce - website to practice selenium | demo website for " \
                               "automation testing | selenium practice sites"
        driver.back()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(text(),'Click Here')]").click()
        assert driver.title == "Page Not Found"

    def tearDown(self):
        driver.close()

