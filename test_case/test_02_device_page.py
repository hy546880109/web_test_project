import os,sys
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(path)
print(path)
from WEB_Test_Project.pages.device_manage_page import Device_Manage_Page
from WEB_Test_Project.pages.login_home_page import LoginPage
from common.parse_excel import ParseExcel

# os.makedirs('cache', exist_ok=True)

def get_test_data():
    '''
    从外部获取参数数据
    :return:
    '''
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_data')
    excelPath = os.path.join(path, 'test_login_user.xlsx')
    sheetName = 'user'
    return ParseExcel(excelPath, sheetName)

class Test_device():

    def setup(self):
        path = os.path.join(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))), 'lib')
        self.url = 'http://106.52.198.240:8899/#/login'
        options = webdriver.ChromeOptions()
        options.add_argument('--disk-cache-dir={}'.format(os.path.join(path, 'cache')))
        self.driver = webdriver.Chrome(executable_path=os.path.join(path, 'chromedriver.exe'), options=options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.device
    def test_drive(self):
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
        sleep(1)
        self.driver.execute_script("document.querySelector('th.el-table_1_column_1.el-table-column--selection.is-leaf > div > label > span > span').click()")
        # self.driver.find_element_by_css_selector('th.el-table_1_column_1.el-table-column--selection.is-leaf > div > label > span > span').click()
        device_page.bukong.click()
        sleep(1)
        device_page.bukong_kuang.click()
        sleep(1)
        self.driver.execute_script("document.querySelector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span').click()")
        device_page.shezhi.click()
        device_page.queding.click()
        sleep(1)
        txt = self.driver.find_element_by_css_selector('#app > div > div.layout-right > div > div.content-box > div > div.manage-table-box > div > div > div > div.manage-table > div > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1) > td.el-table_1_column_8 > div > span').text
        assert '已布防' in txt
        

if __name__ == '__main__':
    pytest.main()