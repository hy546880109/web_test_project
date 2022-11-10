# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : report.py
# @Project: 第51课时

import os
import sys
import platform

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
allure_path = os.path.join(path, 'allure','bin')
sys.path.append(allure_path)

class Report():
    '''报告工具类'''
    @property
    def allure(self):
        if platform.system() == "Windows":
            cmd = os.path.join(allure_path, 'allure.bat')
        else:
            cmd = os.path.join(allure_path, 'allure')
        return cmd
