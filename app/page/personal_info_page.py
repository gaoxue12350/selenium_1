"""
个人信息页面
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.personal_info_setting_page import PersonalInfoSettingPage


class PersonalInfoPage(BasePage):
    def goto_personal_info_setting(self):
        #点击设置按钮
        self.find_and_click(MobileBy.XPATH,'//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[@index=0]')
        return PersonalInfoSettingPage(self.driver)