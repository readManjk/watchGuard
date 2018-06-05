# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:connectionTest.py
@time:2018/06/05 13:09:53
description: 检查connection模块是否能正确获取页面HTML
"""
import unittest
from src.framework.model import connection


class ConnectionTest(unittest.TestCase):

    def setUp(self):
        """
                预置条件:
                        step01. 给定url=https://www.watchguard.com/wgrd-products/appliances-compare

        :return:
        """
        self.url = 'https://www.watchguard.com/wgrd-products/appliances-compare'

    # 检查是否能获取到HTML
    def test_open_url(self):
        page = connection.open_url(self.url)
        if page:
            flag = True
        else:
            flag = False
        self.assertTrue(flag, 'connection.open_url 获取页面失败..')

    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest('test_open_url')
    unittest.TextTestRunner(verbosity=2).run(suite)
