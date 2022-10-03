import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
driver.implicitly_wait(5)
driver.get(
    'https://testautomationpractice.blogspot.com/'
    # 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
)
driver.maximize_window()
action = ActionChains(driver)

# Mouse Hover------------------------------------------
# wait = WebDriverWait(driver, 10)
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#
# configuration = driver.find_element(By.CLASS_NAME, "oxd-topbar-body-nav-tab-item")
# # reporting = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[4]/a')
#

#
# action.move_to_element((configuration)).click().perform()

# Double CLICK------------------------------------------
# copyButton = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')

#
# action.double_click(copyButton).perform()

# Right Click-----------------------------------------

# action.context_click(button).perform() #Right Click Action

# Drag and Drop
# source = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]/img')
# destination = driver.find_element(By.XPATH,'//*[@id="trash"]')
# action.drag_and_drop(source,destination).perform()


time.sleep(2)
driver.close()  # close tab
# driver.quit()#close browser
