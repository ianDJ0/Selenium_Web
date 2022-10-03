from selenium.webdriver.common.by import By

class LoginPage():
    # Locators
    textbox_email = 'Email'
    textbox_password = 'Password'
    button_login = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    button_logout = '//*[@id="navbarText"]/ul/li[3]/a'
    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.textbox_email).clear()
        self.driver.find_element(By.NAME, self.textbox_email).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password).clear()
        self.driver.find_element(By.NAME, self.textbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout).click()