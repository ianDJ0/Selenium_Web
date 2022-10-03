import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))

driver.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select'
    'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
)
driver.switch_to.frame("iframeResult")
driver.find_element(By.ID,'cars').click()
obj = Select(driver.find_element(By.ID,'cars'))
obj.select_by_visible_text("Opel")

time.sleep(3)
driver.close()  # close tab
# driver.quit()#close browser