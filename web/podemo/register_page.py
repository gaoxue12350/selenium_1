from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 注册
    def register(self):
        self.driver.find_element(By.ID, 'corp_name').send_keys('南京互联网公司')
        sleep(1)
        self.driver.find_element(By.ID, 'manager_name').send_keys('林林')
        sleep(1)
        self.driver.find_element(By.ID, 'register_tel').send_keys('13900000000')
        sleep(1)
        self.driver.find_element(By.ID, 'submit_btn').click()
        return True
