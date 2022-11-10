# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : run_test_general_html.py
# @Project: 第51课时

import os
import pytest
import threading
from WEB_Test_Project.common.report import Report

project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
report_dir = os.path.join(project_root, 'report')
result_dir = os.path.join(report_dir, 'allure_result')
allure_report = os.path.join(report_dir, 'allure_report')

report = Report()

# 定义标签，按照指定标签过滤运行用例
tag = "update"

def run_pytest():
    pytest.main(['-v', '-s', "-m", f"{tag}", f'--alluredir={result_dir}'])

def general_report():
    cmd = "{} generate {} -o {} --clean".format(report.allure, result_dir, allure_report)
    print(os.popen(cmd).read())

if __name__ == '__main__':
    run = threading.Thread(target=run_pytest)
    gen = threading.Thread(target=general_report)
    run.start()
    run.join()
    gen.start()
    gen.join()
