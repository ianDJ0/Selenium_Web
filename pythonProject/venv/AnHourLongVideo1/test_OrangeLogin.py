import unittest
import HtmlTestRunner
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class OrangeLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print("Test Started")
        cls.driver = webdriver.Chrome(
            service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
        cls.driver.maximize_window()

    def test_OrangeTitle(self):

        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.assertEqual("OrangeHRM",self.driver.title,"Title does not match")
        time.sleep(2)

    def test_OrangeLogin(self):
        self.driver.implicitly_wait(30)
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
        self.assertEqual("OrangeHRM",self.driver.title,"Title does not match")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()
        print("Test Completed")
if __name__ == "__main__" :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\AnHourLongVideo1/ReportFolder'))