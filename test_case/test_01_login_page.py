# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : test_baidu_home_page_01.py

import os
import sys
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
print(sys.path)
from WEB_Test_Project.pages.login_home_page import LoginPage

# os.makedirs('cache', exist_ok=True)


class TestHomePage():

    def setup(self) -> None:
        path = os.path.join(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))), 'lib')
        self.url = 'http://106.52.198.240:8899/#/login'
        options = webdriver.ChromeOptions()
        options.add_argument('--disk-cache-dir={}'.format(os.path.join(path, 'cache')))
        self.driver = webdriver.Chrome(executable_path=os.path.join(path, 'chromedriver.exe'), options=options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def teardown(self) -> None:
        self.driver.quit()

    @pytest.mark.login
    def test_001_login(self):
        login_home = LoginPage(self.driver)
        login_home.login_user_input.send_keys('admin')
        login_home.login_passwd_input.send_keys('123456')
        login_home.login_yanzheng_input.send_keys('1234')
        login_home.login_button.click()
        assert '管理员' in login_home.login_win_user.text

    def test_002_login(self):
        login_home = LoginPage(self.driver)
        login_home.login_user_input.send_keys('admin')
        login_home.login_passwd_input.send_keys("1234567")
        login_home.login_yanzheng_input.send_keys('1234')
        login_home.login_button.click()
        assert '密码错误' in login_home.login_loss_msg.text

    def test_003_login(self):
        login_home = LoginPage(self.driver)
        login_home.login_user_input.send_keys('admin123')
        login_home.login_passwd_input.send_keys("1234567")
        login_home.login_yanzheng_input.send_keys('1234')
        login_home.login_button.click()
        assert '账户未创建' in login_home.login_loss_msg.text


if __name__ == '__main__':
    pytest.main()
