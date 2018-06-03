# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:visual.py
@time:2018/06/03 17:56:00
@description: 接受逻辑层的数据，然后按照用户需求输出数据
"""
import csv


class Visual(object):

    def __init__(self, file):
        self.file = file

    def write_to_csv(self, title, value):
        """
            @summary 将用户数据写入CSV文件
        :param title: [list] 标题
        :param value: [list] 写入的行数据列表
        :return:
        """
        with open(self.file, 'w', newline="") as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow(title)
            writer.writerows(value)