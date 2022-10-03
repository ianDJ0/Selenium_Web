import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))

driver.get(
    'https://testautomationpractice.blogspot.com/'
)
driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button').click()
driver.switch_to.alert.dismiss()

time.sleep(3)
driver.close()  # close tab
# driver.quit()#close browser