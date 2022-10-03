import unittest

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# driver = webdriver.Chrome(
#     service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
# driver.implicitly_wait(30)
# driver.get(
#     # 'https://testautomationpractice.blogspot.com/'
#     # 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
#     'https://www.amazon.com/'
# )
# # driver.switch_to.frame(0) # activite if on testautomationpractice.blogspot.com
# driver.maximize_window()

class Test(unittest.TestCase):
    def test_firstTest(self):
        print ('this is the first unit test case')

if __name__ == "__main__":
    unittest.main()