"""
编辑联系人页面
"""
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from app.page.base_page import BasePage

class ContactAddPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def add_contact(self,name,gender,phoneNum):
        #添加信息填写
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.find_and_click(MobileBy.XPATH, '//*[contains(@text,"性别")]/..//*[@text="男"]')
        if gender == '男':
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@text="女"]'))
            self.find_and_click(MobileBy.XPATH, '//*[@text="男"]')
        else:
            self.find_and_click(MobileBy.XPATH, '//*[@text="女"]')
        self.find(MobileBy.XPATH, '//*[contains(@text,"手机") and @class="android.widget.EditText"]').send_keys(phoneNum)
        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        from app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)