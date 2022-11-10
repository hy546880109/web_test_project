# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术


from page_objects import PageElement, PageObject  #引入库

class LoginPage(PageObject):
    '''登录首页'''
    login_user_input = PageElement(css="div:nth-child(1) > div > div > div.el-input.el-input--prefix > input")
    login_passwd_input = PageElement(css="div:nth-child(2) > div > div > div > input")
    login_yanzheng_input = PageElement(css="div.putdiv.divmsgcode > div > div > div.msgcon.ellorow > div.hymsgcode.el-input > input")
    login_button = PageElement(css='div.putdiv.divbottom > div > div > button')
    login_win_user = PageElement(css='div > div.header > ul > li.user > span')
    login_loss_msg = PageElement(css='div.right > ul > div > span')
