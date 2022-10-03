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

driver.maximize_window()

# driver.execute_script("window.scrollBy(0,1000)","")#Javacript

# elem = driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[4]/div[1]/form/fieldset[2]/label')
# driver.execute_script("arguments[0].scrollIntoView();",elem)

# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')


time.sleep(2)
driver.close()  # close tab
# driver.quit()#close browser