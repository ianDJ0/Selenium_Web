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
table = driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table')
# driver.current_window_handle
rows = driver.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr[1]')
print(len(rows))
# for row in rows:
#     print(len(rows))
    # Get the columns (all the column 2)
    # col = row.find_elements(By.XPATH, "td")[1] #note: index start from 0, 1 is col 2
    # print (col.text) #prints text from the element
time.sleep(2)
driver.close()  # close tab
# driver.quit()#close browser