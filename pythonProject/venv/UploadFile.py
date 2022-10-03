import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {
    "download.default_directory": "D:\SeleniumDownloadLocation"
})

# driver = webdriver.Chrome()
driver = webdriver.Chrome(
    service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"), chrome_options=chromeOptions)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get(
    # 'https://testautomationpractice.blogspot.com/'
    'https://github.com/operasoftware/operachromiumdriver/releases'
    # 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
)
# driver.switch_to.frame(0)
# driver.find_element(By.ID,'RESULT_FileUpload-10').send_keys('D:\downloads/94a06bec0c2edfd5d1aa7b6ba52815d7.jpg')

driver.find_element(By.XPATH,
                    '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/details/div/div/ul/li[4]/div[1]/a/span').click()

time.sleep(2)
driver.close()  # close tab
# driver.quit()#close browser
