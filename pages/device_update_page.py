# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : device_update_page.py


from page_objects import PageElement, PageObject  #引入库

class Device_Update_Page(PageObject):
    '''设备升级页'''
    shouye_kuozhan = PageElement(css='div.layout-right > div > div.header > div > span')
    device_manage= PageElement(css="div:nth-child(2) > ul > li:nth-child(2) > div > span")
    device_update = PageElement(css="#app > div > div.layout-left > div > div:nth-child(2) > ul > li.el-submenu.is-opened > ul > li > ul > li:nth-child(4)")
    gouxuan_all = PageElement(css="#app > div > div.layout-right > div > div.content-box > div > div:nth-child(2) > div > div.upgrade-table-box > div > div > div > div.upgrade-table > div > div.el-table__fixed > div.el-table__fixed-header-wrapper > table > thead > tr > th.el-table_1_column_1.el-table-column--selection.is-leaf > div > label > span > span")
    zhixing_button = PageElement(css="#app > div > div.layout-right > div > div.content-box > div > div:nth-child(2) > div > div.upgrade-table-box > div > div > div > div.table-operation > div.my-export-button")
    queding_button = PageElement(css='body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')
    yeshu = PageElement(css='#app > div > div.layout-right > div > div.content-box > div > div:nth-child(2) > div > div.upgrade-table-box > div > div > div > div.paging > div > span.el-pagination__sizes > div > div > span > span > i')
    select_yeshu = PageElement(css='body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(5) > span')