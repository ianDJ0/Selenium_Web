import time
import openpyxl
import XLUtilities

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

path = r'D:\SeleniumDownloadLocation/ddt.xlsx'
sheet = "Sheet1"

driver = webdriver.Chrome(
    service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
driver.implicitly_wait(10)
driver.get(
    # 'https://testautomationpractice.blogspot.com/'
    'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
)
# driver.switch_to.frame(0) # activite if on testautomationpractice.blogspot.com
driver.maximize_window()

for r in range(2,XLUtilities.getRowCount(path,sheet)+1):
    driver.find_element(By.NAME, "username").send_keys(XLUtilities.readData(path,sheet,r,2))
    driver.find_element(By.NAME, "password").send_keys(XLUtilities.readData(path,sheet,r,3))
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    if (driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"):
        XLUtilities.writeData(path,sheet,r,5,"Test Passed!")
        time.sleep(3)
        driver.quit()
    else:
        XLUtilities.writeData(path,sheet,r,5,"Test Failed!")


