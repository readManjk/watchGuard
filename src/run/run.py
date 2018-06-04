# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:run.py
@time:2018/06/04 22:04:57
@description: 运行文件
"""
from src.config.default import USER_PRODUCT
from src.framework.controller.control import Control


def begin(user_product):
    """
        @summary 调用control开始运行
    :param user_product: 用户指定的产品类型
    :return: None
    """
    control = Control(user_product)
    control.save_performance_data()


if __name__ == "__main__":
    begin(USER_PRODUCT)
