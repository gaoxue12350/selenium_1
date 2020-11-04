"""
首页
"""
from appium.webdriver.common.mobileby import MobileBy
from app.page.address_list_page import AddressListPage
from app.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver
    address_element=(MobileBy.XPATH, '//*[@text="通讯录"]')
    def goto_message(self):
        pass

    def goto_address(self):
        # 进到通讯录页面
        # self.find(*self.address_element).click()
        self.find_and_click(*self.address_element)
        return AddressListPage(self.driver)