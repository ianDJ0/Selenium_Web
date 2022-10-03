import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class searchEngineTest(unittest.TestCase):

    # def test_search(self):
    #     self.driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
    #     self.driver.get('https://www.google.com/')
    #     self.assertEqual('Google',self.driver.title, "Web page title is not same")
    #     self.driver.quit()

    def test_advancedSearch(self):
        fruits = {'apple','orange','dragonfruit'}
        self.assertIn('apple',fruits,"Fruit is not in the list")
    #
    #
    # def test_imageSearch(self):
    #     self.driver = webdriver.Chrome(
    #         service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
    #     self.driver.get('https://www.google.com/')
    #     print(f"This is image Search")
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
