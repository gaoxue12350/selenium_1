"""
编辑成员页面
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage


class EditMemeberPage(BasePage):
    def delete_member(self):
        #删除成员
        self.find_by_scroll('删除成员').click()
        self.find_and_click(MobileBy.XPATH,'//*[@text="确定"]')
        from app.page.address_list_page import AddressListPage
        return AddressListPage(self.driver)