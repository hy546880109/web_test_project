from selenium import webdriver
import os,sys,json
import pytest
from time import sleep
import shutil
from selenium.webdriver.support.select import Select
from pathlib import Path
import pandas as pd
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from WEB_Test_Project.pages.device_update_page import Device_Update_Page
from WEB_Test_Project.pages.login_home_page import LoginPage
from WEB_Test_Project.pages.device_manage_page import Device_Manage_Page


my_file = r'F:\download'
down_file = Path(my_file)
class Test_device():

    def setup(self):
        if down_file.is_dir():
            shutil.rmtree(my_file)    #强制删除文件夹
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
        self.url = 'http://106.52.198.240:8899/#/login'
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": my_file}
        #添加指定下载路径
        options.add_experimental_option("prefs", prefs)
        #添加指定缓存路径
        options.add_argument('--disk-cache-dir={}'.format(os.path.join(path, 'cache')))
        self.driver = webdriver.Chrome(executable_path=os.path.join(path, 'chromedriver.exe'), options=options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.search
    def test_devcie_search(self):

        login_home = LoginPage(self.driver)
        login_home.login_user_input.send_keys('admin')
        login_home.login_passwd_input.send_keys("123456")
        login_home.login_yanzheng_input.send_keys('1234')
        login_home.login_button.click()
        device_page = Device_Manage_Page(self.driver)
        device_page.shouye_kuozhan.click()
        sleep(1)
        device_page.device_tubiao.click()
        device_page.device_manage.click()
        device_page.imei_search.send_keys('868030912507007')
        device_page.name_search.send_keys('测试')
        device_page.mac_search.send_keys('DE:E4:7A:DE:CF:35')
        device_page.iccid_search.send_keys('30003052258000915503')
        # device_page.device_type_search.click()
        # device_page.device_type_search_lora.click()
        # device_page.quyu_search.click()
        # b = device_page.quyu_search_guangdong
        # self.driver.execute_script("arguments[0].click();", b)
        # c = device_page.quyu_search_guangdong_shenzhen
        # self.driver.execute_script("arguments[0].click();", c)
        device_page.start_time_search.send_keys('2021-11-08')
        device_page.end_time_search.send_keys('2022-11-08')
        device_page.chaxun.click()
        device_page.daochu.click()
        device_page.daochu_queding.click()
        device_page.daochu_queding_queren.click()
        sleep(1)
        path_xlsx = os.listdir(my_file)
        for f in path_xlsx:
            df = pd.read_excel(my_file +'\\'+ str(f))
            data = df.values.tolist()[0]
        assert  868030912507007 in data
        assert  '测试' in data
        assert '868030912507007' ==  device_page.imei.text







