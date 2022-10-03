import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
driver.implicitly_wait(10)
driver.get(
    'https://www.accenture.com/ph-en'
    # "https://my.forms.app/arpeemcallejo-arruejo/my-untitled-form"
)
# driver.find_element("xpath",'//*[@id="form-content"]/div/div/div/div/div/div[2]/div')
path = "D:\PyCharm"
elements = driver.find_elements(By.TAG_NAME, 'a')
for a in elements:
    print(a.get_attribute("href"))
    driver.save_screenshot(f'D:\\PyCharm\\{re.sub(r"[^a-zA-Z0-9 ]","",a.get_attribute("href"))}{time.strftime("%m_%d_%Y %H%M%S")}.png')

    # # Loading the image
    # image = Image.open("image.png")
    #
    # # Showing the image
    # image.show()
    # # bod = driver.find_elements(By.TAG_NAME,"body")



# email = driver.find_element(by=By.NAME, value='email')
# password = driver.find_element(by=By.NAME, value='pass')
#
# email.send_keys("correct")
# # password.send_keys("Wrong")
#
# driver.find_element(by=By.NAME, value='login').click()

time.sleep(5)
driver.close()  # close tab
# driver.quit()#close browser