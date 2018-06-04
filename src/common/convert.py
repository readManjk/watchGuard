# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:convert.py
@time:2018/06/04 20:32:33
@description: Gbps Mbps 转换
"""


def data_flow(value):
    """
        将特定格式的Gbps Mbps 转换成Kbps
    :param value: 待转换值
    :return:返回KB单位的数字
    """
    # 取数字
    digit = value.split(' ')[0]
    digit = float(digit)
    if 'Kbps' in value:
        data = value
    elif 'Mbps' in value:
        data = digit * 1024
    elif 'Gbps' in value:
        data = digit * 1024 * 1024
    return data

