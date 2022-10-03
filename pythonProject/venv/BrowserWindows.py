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
driver.find_element(By.XPATH,'//*[@id="Attribution1"]/div[1]/a[2]').click()
# driver.current_window_handle
windows = driver.window_handles
for window in windows:
    driver.switch_to.window((window))
    if(driver.current_url == "https://testautomationpractice.blogspot.com/"):
        driver.close()
time.sleep(2)
driver.close()  # close tab
# driver.quit()#close browser