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
driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a").click()
time.sleep(1)
email = driver.find_element(by=By.ID, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input')
password = driver.find_element(by=By.NAME, value='pass')

print (email.is_selected())


time.sleep(5)
driver.close()  # close tab
# driver.quit()#close browser