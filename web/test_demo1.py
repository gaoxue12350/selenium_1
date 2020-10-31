import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Testdemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        sleep(3)

    def test_cookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # cookies=self.driver.get_cookies()
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853100647697'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '02Od1pusxuDJVqcpy2HR6uAYZebqgdZ5U8XGy4Ck9PFP7lKKDiJGsmQg5nDpyhkS81Vkxg3c8uwp-kUaoP_g28XIkObZQj49w16S-wqb5T2uZLVkMFZWlYMwR-WXULf9lQheLXE4PdYRYW51YNmkXvOn49kA_1Khe-3qLph8rDEjgKbBvhaYQrouOZIhT-G-uFa6Db3hvdf3DeS4R33sBJ4hqIb46W-UPsgI980_GWSl0k6NUZY5OBiYGyZeBJY1bOrGxB4BIiUE_GDyvFWM2A'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325056160818'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4352981'},
            {'domain': '.qq.com', 'expiry': 1603603673, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603623667, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '67hh682'},
            {'domain': '.qq.com', 'expiry': 1603690023, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.895886440.1603592135'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '24882760801613442'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'TKhmMy_8WKsH9tO7m1tzCO3c4xqofCd574mBDA6AylZggrCiv26CFZD-9T2Hxrvf'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635128131, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635128132, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1603592133'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606195634, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853100647697'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1603623667, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '67hh682'},
            {'domain': '.qq.com', 'expiry': 1666675623, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1815757775.1603592135'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '4799267879'},
            {'domain': '.qq.com', 'expiry': 1916140641, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': 'e833591a13942dea'}]
        # cookies=self.driver.get_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(3)

    def test_shelve(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # shelve python内置模块，用来对数据进行持久化存储，相当于小型的数据库
        # 可以通过key,value把数据保存到shelve中
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(3)
        # 点击导入联系人
        self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        sleep(3)
        # 点击文件上传
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[1]/a/input').send_keys(
            '/Users/gaoxue/Desktop/test1.xlsx')
        sleep(3)
        # 获取上传的文件名
        filename = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[1]/div[2]').text
        assert filename == 'test1.xlsx'
