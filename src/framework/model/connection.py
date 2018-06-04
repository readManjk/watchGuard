# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:connection.py
@time:2018/06/03 16:49:28
"""
import requests
from src.common.log import Log
from src.common.myexception import RequestHostFailed

log = Log('connect')


def open_url(url):
    """
        @summary 根据指定的URL 获取网页内容
    :param url: [str] 网页url
    :return data: [str] 网页内容
    """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    try:
        res = requests.get(url, headers=header)
    except Exception as e:
        log.exception('连接被服务器强制断开，请重新尝试...[%s]' % str(e))
        RequestHostFailed('request请求被服务器强制断开')
    if res.status_code == 200:
        data = res.text
    else:
        data = ""
    return data
