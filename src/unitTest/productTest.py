# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:productTest.py
@time:2018/06/05 12:25:49
description: 测试product模块能否正确获取产品属性
"""
import unittest
from src.framework.model.product import Product
from src.framework.model import connection


class ProductTest(unittest.TestCase):
    def setUp(self):
        """
                # 预置条件：
                    Step01.已选择WatchGuard Firebox® M440产品，产品value值1320，产品url：
                         https://www.watchguard.com/wgrd-products/appliances-compare/1320/1320/1320
                    Step02.设置变量name =WatchGuard Firebox® M440, data = ['Firewall Throughput', 'VPN Throughput',
                           'AV Throughput', 'IPS Throughput','UTM Throughput', 'Concurrent Sessions*']
                    Step02.获取产品HTML，实例化产品对象
        """
        self.url = "https://www.watchguard.com/wgrd-products/appliances-compare/1320/1320/1320"
        self.data = ['Firewall Throughput', 'VPN Throughput', 'AV Throughput', 'IPS Throughput',
                     'UTM Throughput', 'Concurrent Sessions*']
        self.name = 'WatchGuard Firebox® M440'
        # 获取html
        page = connection.open_url(self.url)
        self.product = Product(self.name, page)

    # case01. 检查产品name属性是否等于WatchGuardFirebox® M440
    def test_product_name(self):
        find_name = ""
        if self.product.tr_tag:
            # 取出name值
            tr = self.product.tr_tag[1]
            th_tag = tr.find_all('th')[1]
            find_name = th_tag.text
        self.assertEqual(self.name, find_name, "查找出的产品name和实例化Product不一致")

    # case02. 调用产品get_product_performance接口，检查返回的键值是否都在data列表中
    def test_product_performance_data(self):
        performance_data = self.product.get_product_performance()
        flag = True
        find_key_list = []
        for k, v in performance_data.items():
            find_key_list.append(k)
        # 检查需要的参数是否都已获取
        for i in self.data:
            if i not in find_key_list:
                flag = False
        self.assertTrue(flag, '获取的performance数据中包含非performance数据')

    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest('test_product_name')
    suite.addTest('test_product_performance_data')
    unittest.TextTestRunner(verbosity=2).run(suite)
