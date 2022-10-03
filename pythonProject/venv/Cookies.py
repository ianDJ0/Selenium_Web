import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

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

#Get Cookies created by the browser
cookies = driver.get_cookies()
print (len(cookies)) # Print cookies created in the browser
print(cookies)

#Adding Cookies to the browser
cookie={'name':'My Cookie', 'value':"987564"}
driver.add_cookie(cookie)

# Delete Cookie
driver.delete_cookie('My Cookie')
cookies = driver.get_cookies()
print (len(cookies)) # Print cookies created in the browser
print(cookies)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))