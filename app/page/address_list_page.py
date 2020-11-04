"""
通讯录页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from app.page.base_page import BasePage
from app.page.member_invite_menu_page import MemberInviteMenuPage
from app.page.personal_info_page import PersonalInfoPage


class AddressListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def click_addmember(self):
        # 滚动查找添加成员
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def goto_personal_info(self,name):
        #进入个人信息页面
        self.find_by_scroll(name).click()
        return PersonalInfoPage(self.driver)

    def find_member(self, name):
        #寻找成员，能找到返回True，找不到返回False
        result = True
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hxw')
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        try:
            self.find(MobileBy.XPATH, '//*[@text="name11" and @clickable="false"]')
        except NoSuchElementException:
            result = False
        else:
            result = True
        return result