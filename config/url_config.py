#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : url_config.py


import enum

class Conf(enum.Enum):
    '''
    环境配置枚举类
    '''
    INDEX_URL = 'https://www.baidu.com'
    NEWS_URL= 'http://news.baidu.com/'

    port = 3306
    user = 'root'

    host = '139.159.202.43'

if __name__ == '__main__':
    print(Conf.INDEX_URL.name)
    print(Conf.INDEX_URL.value)

