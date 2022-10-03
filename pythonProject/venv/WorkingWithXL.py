import time
import openpyxl

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

path = 'D:\SeleniumDownloadLocation/ddt.xlsx'
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(
#     service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))

workbook = openpyxl.load_workbook(path)

sheet = workbook.active # or workbook[sheetName]

row = sheet.max_row
cols = sheet.max_column
print(f'{row} {cols}')
for r in range(1,row+1):
    for c in range(1, cols+1):
        print(f'{sheet.cell(row=r, column=c).value}',end="   ")
    print('')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get(
#     # 'https://testautomationpractice.blogspot.com/'
#     'https://github.com/operasoftware/operachromiumdriver/releases'
#     # 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
# )

# time.sleep(2)
# driver.close()  # close tab
# driver.quit()#close browser
