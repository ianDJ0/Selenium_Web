import allure
import pytest
import allure_pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
class TestLogin():
    baseURL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username = 'Admin'
    password = 'admin1234'

    # @pytest.fixture() # setUp
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(
            executable_path="C://Users//Potato//PycharmProjects//pythonProject//venv//AnHourLongVideo1//Drivers//chromedriver.exe"))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        yield
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_Login(self, setup):
        self.driver.get(self.baseURL)
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, 'password').clear()

        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        assertControl = self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
        if(assertControl):
            assert assertControl
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Test Login Page",
                          attachment_type=AttachmentType.PNG)
            assert assertControl
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()

        time.sleep(2)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Title(self, setup):
        self.driver.get(self.baseURL)
        assert self.driver.title == 'OrangeHRM'

    @allure.severity(allure.severity_level.NORMAL)
    def test_advance(self):
        pytest.skip("The test will later be implemented")

# pytest -v  --html=.\reports\report.html  test_PytestDemo1.py
# pytest -v -s --html=.\reports\report.html --self-contained-html test_PytestDemo1.py ----------------simple pytest generated report
# pytest -v --alluredir="./ReportsFolder/" test_AllureDemo.py
# allure serve "C:\Users\Potato\PycharmProjects\pythonProject\venv\AllureDemo\ReportsFolder"