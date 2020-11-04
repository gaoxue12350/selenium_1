"""
个人信息设置页面
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.edit_member_page import EditMemeberPage


class PersonalInfoSettingPage(BasePage):
    def goto_edit_member(self):
        #点击编辑成员
        self.find_and_click(MobileBy.XPATH,'//*[@text="编辑成员"]')
        return EditMemeberPage(self.driver)