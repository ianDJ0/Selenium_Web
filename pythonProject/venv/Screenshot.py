import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
driver.implicitly_wait(30)
driver.get(
    # 'https://testautomationpractice.blogspot.com/'
    # 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    'https://www.amazon.com/'
)
# driver.switch_to.frame(0) # activite if on testautomationpractice.blogspot.com
driver.maximize_window()

# Saving Screenshot
driver.save_screenshot('D:\SeleniumDownloadLocation/amazon.png')
