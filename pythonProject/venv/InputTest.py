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


# inputboxes =
# password = driver.find_element(by=By.NAME, value='lname')

drop=Select(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/div/div[1]/form[1]/select'))

drop.select_by_visible_text("CSS")



# email.send_keys("correct")
# password.send_keys("Wrong")

# driver.find_element(by=By.NAME, value='login').click()

time.sleep(5)
driver.close()  # close tab
# driver.quit()#close browser