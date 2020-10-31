from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo1.page.add_member_page import AddMemberPage
from web.podemo1.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # def __init__(self):
    #     options=Options()
    #     options.debugger_address='127.0.0.1:9222'
    #     self.driver=webdriver.Chrome(options=options)

    def goto_addMember(self):
        # #点击添加联系人
        # #self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        # return AddMemberPage(self.driver)

        # 点击通讯录
        locator = self.find(By.CSS_SELECTOR, '#menu_contacts')
        locator.click()
        # self.driver.find_element(By.CSS_SELECTOR,'#menu_contacts').click()
        sleep(2)
        # 点击添加成员
        self.find(By.CSS_SELECTOR, '.js_has_member>div>a:nth-child(2)').click()

        def wait_for_next(x: WebDriver):
            try:
                x.find_elements(*locator).click()
                return x.find_element(By.ID, 'username')
            except:
                return False

        WebDriverWait(self.dirver, 10).until(wait_for_next)
        return AddMemberPage(self.driver)
