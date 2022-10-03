import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(executable_path="D:\PyCharm\chromedriver_win32\chromedriver.exe"))
driver.get("https://www.google.com/search?q=logout+logo+png&sxsrf=ACYBGNTW1Hb_V7wZY8NxWw-kqhjodYm9kA:1573378656293&source=lnms&tbm=isch&sa=X&ved=0ahUKEwih7p6frN_lAhWDIbcAHcI_D1kQ_AUIEigB&biw=1920&bih=937#imgrc=syi6fRcyFmYJAM:")

print (driver.title) #title of the page
driver.find_element("xpath","//*[@id='yDmH0d']/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]").click()

time.sleep(3)
driver.close() #close tab
# driver.quit()#close browser