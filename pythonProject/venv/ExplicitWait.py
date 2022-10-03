
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
driver.implicitly_wait(8)
driver.get(
    "https://www.expedia.com/"
)
driver.maximize_window()
driver.find_element(by=By.XPATH, value='//*[@id="wizardMainRegionV2"]/  div/div/div/div/ul/li[6]/a').click()
# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/div/div/div/div/div/div/form/div[2]/div[1]/div/select').click()
destination = driver.find_element(by=By.XPATH,value='//*[@id="cruise-destination"]')
destination.send_keys("ASIA")
driver.find_element(by=By.XPATH, value='//*[@id="wizard-cruise-pwa-1"]/div[3]/div[2]/button').click()

wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sailingVariety-ocean-ember923"]')))

element.click()

time.sleep(4)
driver.close()  # close tab
# driver.quit()#close browser