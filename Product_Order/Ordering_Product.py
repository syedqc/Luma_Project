import datetime
import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class product_order(unittest.TestCase):
    def setUp(self):
        global driver
        cur_time = datetime.datetime.now()
        print(cur_time)
        ch_options = Options()
        ch_options.add_experimental_option("detach", True)
        ch_options.add_argument("--incognito")
        driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", options=ch_options)
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.implicitly_wait(3)
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

    def test_order(self):
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@id='search']").send_keys("Cronus Yoga Pant ")
        driver.find_element(By.XPATH, "//input[@id='search']").send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "//a[contains(text(),'Cronus Yoga Pant')]").click()
        driver.find_element(By.XPATH, "//div[@aria-label='34']").click()
        driver.find_element(By.XPATH, "//div[@option-label='Black']").click()
        driver.find_element(By.XPATH, "//button[@id='product-addtocart-button']").click()
        # driver.find_element(By.XPATH, "//header/div[2]/div[1]/a[1]/span[2]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@class='action showcart']").click()
        driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@data-role='opc-continue']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[contains(text(),'Place Order')]").click()
        suc_alert = driver.find_element(By.XPATH, "//span[contains(text(),'Thank you for your purchase!')]").text
        if suc_alert == "Thank you for your purchase!":
            print("Test Pass -Order is placed successfully")
        else:
            print("Test Fail -Unable to place order")
        print(driver.find_element(By.XPATH, "//a[@class='order-number']").text)


if __name__ == '__main__':
    unittest.main()
