import time
import logging
import os
import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class TestLogin():
    baseURL = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'

    # @pytest.fixture() # setUp
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(
            executable_path="C://Users//Potato//PycharmProjects//pythonProject//venv//AnHourLongVideo1//Drivers//chromedriver.exe"))
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_Login(self, setup):
        username = 'admin@yourstore.com'
        password = 'admin'
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.NAME, "Email").clear()
        self.driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")

        self.driver.find_element(By.NAME, 'Password').clear()
        self.driver.find_element(By.NAME, 'Password').send_keys('admin')
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
        time.sleep(2)
        assert self.driver.title == 'Dashboard / nopCommerce administration'
        path = os.path.join('C:/Users/Potato/Desktop/New folder/',f'{self.driver.title.replace("/","")}')
        os.mkdir(path)
        print()
        self.driver.save_screenshot(f'{path}/amazon.png')
        self.driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[3]/a').click()
        time.sleep(2)

    def test_Title(self, setup):
        self.driver.get(self.baseURL)
        assert self.driver.title == 'Your store. Login'
