import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):

    def test_search(self):
        self.driver = webdriver.Chrome(
            service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
        self.driver.implicitly_wait(30)
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
        self.assertTrue('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login' == self.driver.current_url,
                        "URL does not match")
        time.sleep(2)
        self.driver.quit()

    def test_advancedSearch(self):
        fruits = {'apple','orange','dragonfruit'}
        self.assertIn('apple',fruits,"Fruit is not in the list")

    def test_imageSearch(self):
        self.driver = webdriver.Chrome(
            service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
        self.driver.get('https://www.google.com/')
        self.assertEqual('Google',self.driver.title,"Title does not match")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
