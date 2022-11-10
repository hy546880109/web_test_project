# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : run_test_general_html.py
# @Project: 第51课时

import os
import time
import pytest

project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
report_dir = os.path.join(project_root, 'report')
print(report_dir)
# 测试报告地址
current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
report_abspath = os.path.join(report_dir, "HTMLReport_{}.html".format(current_time))
print(report_abspath)

# 定义标签，按照指定标签过滤运行用例
tag = "search"

if __name__ == '__main__':
    # pytest.main(['-v','-s',"-m", f"{tag}",f'--html={report_abspath}','--self-contained-html'])
    pytest.main(['-v','-s',f'--html={report_abspath}','--self-contained-html'])