import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))

driver.get(
    "https://www.facebook.com/"
)

email = driver.find_element(by=By.NAME, value='email')
password = driver.find_element(by=By.NAME, value='pass')

email.send_keys("correct")
password.send_keys("Wrong")

driver.find_element(by=By.NAME, value='login').click()
driver.implicitly_wait(10)

driver.close()  # close tab
# driver.quit()#close browser