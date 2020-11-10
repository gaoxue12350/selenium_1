import yaml
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from frame1.hand_black import handle_black


class BasePage:
    # black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0
    with open('./base_page.yaml') as f:
        data = yaml.load(f)
        caps = data['caps']
        ip = data['server']['ip']
        port = data['server']['port']
        #黑名单列表
        black_list = data['black_list']

    def __init__(self, driver: WebDriver = None):
        """
        初始化应用
        """
        if driver is None:
            # caps = {}
            # caps["platformName"] = "android"
            # caps["deviceName"] = "test1"
            # caps["appPackage"] = "com.xueqiu.android"
            # caps["appActivity"] = ".view.WelcomeActivityAlias"
            # caps["noReset"] = "true"
            # caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化安装（appium settings）
            # caps['skipServerInstallation'] = 'true'
            # caps["settings[waitForIdleTimeout]"] = 0
            # with open('./base_page.yaml') as f:
            #     data=yaml.load(f)
            #     caps=data['caps']
            #     # print(caps,type(caps))
            #     ip=data['server']['ip']
            #     port=data['server']['port']
                # print(caps,type(caps))
            self.driver = webdriver.Remote(f"http://{self.ip}:{self.port}/wd/hub", self.caps)
            self.driver.implicitly_wait(15)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """
        if locator is None:
            # 如果传的元素是一个，只有 by
            result = self.driver.find_element(*by)
        else:
            # 如果传的元素是二个，既有 by ，又有 locator
            result = self.driver.find_element(by, locator)
        return result

    def parse_yaml(self,path,func_name):
        with open(path,encoding='utf-8') as f:
            data=yaml.load(f)
        self.parse(data[func_name])

    def parse(self,steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'],step['locator']).click()
            elif 'send' == step['action']:
                self.find(step['by'],step['locator']).send_keys(step['content'])