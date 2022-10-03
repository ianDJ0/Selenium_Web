import unittest
import HtmlTestRunner
import time
# import sys
# sys.path.append('C://Users//Potato//PycharmProjects//pythonProject//venv//AnHourLongVideo1//PageObjects//LoginPage.py')

from AnHourLongVideo1.PageObjects.LoginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):
    baseURL = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
    username = 'admin@yourstore.com'
    password = 'admin'

    driver = webdriver.Chrome(
        service=Service(
            executable_path="C://Users//Potato//PycharmProjects//pythonProject//venv//AnHourLongVideo1//Drivers//chromedriver.exe"))

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_OrangeLogin(self):
        login = LoginPage(self.driver)
        self.driver.implicitly_wait(30)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()
        time.sleep(2)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Title does not match")
        login.clickLogout()
        time.sleep(2)

    def test_OrangeTitle(self):
        self.assertEqual("Your store. Login", self.driver.title, "Title does not match")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../ReportFolder'))
