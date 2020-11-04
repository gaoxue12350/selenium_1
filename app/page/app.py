"""
存放app相关操作，比如启动、重启、停止、进入到首页
"""
import yaml
from appium import webdriver
from app.page.base_page import BasePage
from app.page.main_page import MainPage

with open('../datas/caps.yml') as f:
    myconfig=yaml.safe_load(f)
    caps=myconfig['desirecaps']
    ip=myconfig['server']['ip']
    port=myconfig['server']['port']

class App(BasePage):
    def start(self):
        if self.driver==None:
            # caps={}
            # caps['platformName'] = "Android"
            # caps["deviceName"] = "hogwarts"
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            # # noReset 保留缓存， 比如登录状态
            # caps["noReset"] = "True"
            # # 不停止应用，直接运行测试用例
            # # caps["dontStopAppOnReset"] = "true"  # 测试过程中不会kill应用，直接完成页面操作
            # caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化安装（appium settings）
            # caps['skipServerInstallation'] = 'true'
            # caps["settings[waitForIdleTimeout]"] = 0
            # 关键  localhost:4723  本机ip:server端口
            # print(caps,type(caps))
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

        return  self  #返回在当前页面，保持不动


    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self)->MainPage:
        return MainPage(self.driver)