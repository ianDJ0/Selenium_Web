import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class searchEngineTest(unittest.TestCase):

    def test_Google(self):
        self.driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
        self.driver.get(
            # 'https://testautomationpractice.blogspot.com/'
            # 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
            'https://www.google.com/'
        )
        # driver.switch_to.frame(0) # activite if on testautomationpractice.blogspot.com

        print(f"Title of the Page: {self.driver.title}")
        self.driver.quit()

    def test_GoogleSearch(self):
        self.driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
        self.driver.get('https://www.amazon.com/')
        print(f"Title of the Page: {self.driver.title}")
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()