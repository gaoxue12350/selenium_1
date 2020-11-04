"""
基类模块：初始化driver，定义find，常用的基本方法
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def find(self,by,locator):
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by,locator)

    def find_and_click(self,by,locator):
        logging.info('click')
        return self.find(by,locator).click()

    def find_by_scroll(self,text):
        logging.info('find_by_scroll')
        logging.info(text)
        return  self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                         f'new UiScrollable(new UiSelector()\
                                         .scrollable(true).instance(0))\
                                         .scrollIntoView(new UiSelector()\
                                         .text("{text}").instance(0));')

    def get_toast_text(self):
        logging.info('get_toast_text')
        result=self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        logging.info(result)
        return result