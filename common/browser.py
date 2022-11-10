# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : browser.py

import os
from enum import Enum
import sys
import platform
from selenium import webdriver

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.append(path)
print(path)
class BrwoserType(Enum):
    '''浏览器驱动对应关系'''

    if platform.system() == "Windows":
        chrome = 'chromedriver.exe'
        edge = 'msedgedriver.exe'
        firefox = 'geckodriver.exe'
    else:
        chrome = 'chromedriver'
        edge = 'msedgedriver'
        firefox = 'geckodriver'


class Browser(object):
    '''选择浏览器，并返回实例化浏览器对象'''

    @staticmethod
    def open_browser(type):
        if type == 'chrome':
            driver = webdriver.Chrome(executable_path=os.path.join(path, BrwoserType.chrome.value))
        elif type == 'edge':
            driver = webdriver.Edge(executable_path=os.path.join(path, BrwoserType.edge.value))
        elif type == 'firefox':
            driver = webdriver.Firefox(executable_path=os.path.join(path, BrwoserType.firefox.value))
        else:
            driver = webdriver.Chrome(executable_path=os.path.join(path, BrwoserType.chrome.value))
        return driver
