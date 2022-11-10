# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : baidu_search_page.py


from page_objects import PageElement, PageObject,MultiPageElement  #引入库
from WEB_Test_Project.pages.login_home_page import LoginPage

class Device_Manage_Page(LoginPage):
    '''设备管理界面'''
    shouye_kuozhan = PageElement(css='div.layout-right > div > div.header > div > span')
    device_tubiao = PageElement(css="div:nth-child(2) > ul > li:nth-child(2) > div > span")
    device_manage = PageElement(css="div:nth-child(2) > ul > li.el-submenu.is-opened > ul > li > ul > li:nth-child(2)")
    device_gouxuan = PageElement(css='tr:nth-child(1) > td.el-table_1_column_1.el-table-column--selection > div > label > span > span')
    bukong = PageElement(css='div.table-operation > div.my-export-button')
    bukong_kuang = PageElement(css='form > div.itemrowform.el-row > div > div > div > div.el-input.el-input--suffix > input')
    bukong_status = PageElement(css='div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.hover > span')
    shezhi = PageElement(css='form > div.el-form-item > div > div > span.juleft > div')
    queding = PageElement(css='button.el-button.el-button--default.el-button--small.el-button--primary > span')
    imei_search = PageElement(css='div.el-card.is-always-shadow > div > div > ul > li:nth-child(2) > div > input')
    name_search = PageElement(css='div.el-card.is-always-shadow > div > div > ul > li:nth-child(3) > div > input')
    mac_search = PageElement(css='div.el-card.is-always-shadow > div > div > ul > li:nth-child(4) > div > input')
    iccid_search = PageElement(css='div.el-card.is-always-shadow > div > div > ul > li:nth-child(5) > div > input')
    device_type_search = PageElement(css='#app > div > div.layout-right > div > div.content-box > div > div.el-card.is-always-shadow > div > div > ul > li:nth-child(6) > div > div.el-input.el-input--suffix > input')
    device_type_search_lora = PageElement(xpath='/html/body/div[2]/div[1]/div[1]/ul/li[5]')
    sofa_version_search = PageElement(css='#app > div > div.layout-right > div > div.content-box > div > div.el-card.is-always-shadow > div > div > ul > li:nth-child(7) > div > div.el-input.el-input--suffix > input')
    quyu_search = PageElement(css='#app > div > div.layout-right > div > div.content-box > div > div.el-card.is-always-shadow > div > div > ul > li:nth-child(8) > div > div.el-input.el-input--suffix > input')
    quyu_search_guangdong = PageElement(xpath='/html/body/div[3]/div[1]/div/div[1]/ul/li[19]/label')
    quyu_search_guangdong_shenzhen = PageElement(xpath='/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[3]/label')
    start_time_search = PageElement(css='div.el-card.is-always-shadow > div > div > ul > li.overmaxstep > div > input:nth-child(2)')
    end_time_search = PageElement(css='div.el-card.is-always-shadow > div > div > ul > li.overmaxstep > div > input:nth-child(4)')
    chaxun = PageElement(css='div.el-card.is-always-shadow > div > div > div > div.my-inquire-button')
    imei = PageElement(css='div.manage-table-box > div > div > div > div.manage-table > div > div.el-table__fixed > div.el-table__fixed-body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_2 > div')
    daochu = PageElement(css='#app > div > div.layout-right > div > div.content-box > div > div.el-card.is-always-shadow > div > div > div > div.my-export-button')
    daochu_queding = PageElement(css='#app > div > div.layout-right > div > div.content-box > div > div.warninfotank.daochutankbox > div > div > div.el-dialog__body > div > form > div.el-form-item > div > div > span.juleft > div')
    daochu_queding_queren = PageElement(css='body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span')