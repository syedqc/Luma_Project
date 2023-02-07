import datetime
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Searchbar_secanrios(unittest.TestCase):
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

    def test_search_valid(self):
        search_key = driver.find_element(By.XPATH, "//input[@id='search']")
        search_key.send_keys("Cronus Yoga Pant")
        search_key.send_keys(Keys.ENTER)
        search_results = driver.find_element(By.XPATH, "//a[contains(text(),'Cronus Yoga Pant')]").text
        if search_results == "Cronus Yoga Pant":
            print("Test Pass -With valid search term")
        else:
            print("Test Fail -Report Bug valid search term")

    def test_search_invalid(self):
        search_key = driver.find_element(By.XPATH, "//input[@id='search']")
        search_key.send_keys("Ram")
        search_key.send_keys(Keys.ENTER)
        search_results = driver.find_element(By.XPATH,
                                             "//div[contains(text(),'Your search returned no results.')]").text
        if search_results == "Your search returned no results.":
            print("Test Pass -With invalid search term")
        else:
            print("Test Fail -Report Bug invalid search term")

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()
