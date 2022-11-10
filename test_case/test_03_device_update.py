import os,sys,pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from WEB_Test_Project.pages.device_update_page import Device_Update_Page
from WEB_Test_Project.pages.login_home_page import LoginPage
from WEB_Test_Project.pages.device_manage_page import Device_Manage_Page
from WEB_Test_Project.common.err_screen import errorScreen


class Test_Device_Update():

    def setup(self):
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'lib')
        self.url = 'http://106.52.198.240:8899/#/login'
        options = webdriver.ChromeOptions()
        options.add_argument('--disk-cache-dir={}'.format(os.path.join(path, 'cache')))
        self.driver = webdriver.Chrome(executable_path=os.path.join(path, 'chromedriver.exe'), options=options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.update
    @errorScreen
    def test_device_update(self):
        login_home = LoginPage(self.driver)
        login_home.login_user_input.send_keys('admin')
        login_home.login_passwd_input.send_keys("123456")
        login_home.login_yanzheng_input.send_keys('1234')
        login_home.login_button.click()
        device_page = Device_Update_Page(self.driver)
        device_page.shouye_kuozhan.click()
        sleep(1)
        device_page.device_manage.click()
        device_page.device_update.click()
        device_page.yeshu.click()
        device_page.select_yeshu.click()
        device_page.gouxuan_all.click()
        device_page.zhixing_button.click()
        device_page.queding_button.click()
        txt = self.driver.execute_script("document.querySelector('#app > div > div.layout-right > div > div.content-box > div > div:nth-child(2) > div > div.upgrade-table-box > div > div > div > div.upgrade-table > div > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1) > td.el-table_1_column_3 > div').textContent")
        assert 'cs' == txt

if __name__ == '__main__':
    pytest.main()