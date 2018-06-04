# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:product.py
@time:2018/06/03 23:50:38
"""
from bs4 import BeautifulSoup
from src.config.default import PERFORMANCE
from src.framework.model import connection


class Product(object):

    def __init__(self, name, page):
        self.name = name
        self.page = page
        self.tr_tag = self._get_tr_tag()

    def get_product_hardware(self):
        """
            @summary 获取产品的硬件数据
        :return:
        """
        pass

    def get_product_security(self):
        """
            @summary 获取产品的安全数据
        :return:
        """
        pass

    def get_product_performance(self):
        """
            @summary 获取产品的性能数据
        :return performance_data: 以列表形式返回，其中元素是字典(key：性能名称，value：性能数据)
        """
        performance_data = []
        for tr in self.tr_tag:
            td = tr.find_all('td')
            for index, v in enumerate(td):
                if v.text and str(v.text).strip() in PERFORMANCE:
                    performance_data.append({v.text: td[index + 1].text})
        return performance_data

    def get_product_vpn_tunnels(self):
        """
            @summary 获取产品的VPN TUNNELS 数据
        :return:
        """
        pass

    def get_product_networking_feature(self):
        """
            @summary 获取产品networking feature
        :return:
        """
        pass

    def _get_tr_tag(self):
        """
            @summary 获取tr 标签列表
        :return:
        """
        soup = BeautifulSoup(self.page, features='lxml')
        table_tag = soup.find_all("table")
        if table_tag:
            tr_tag = table_tag[0].find_all('tr')
        else:
            tr_tag = []
        return tr_tag


if __name__ == "__main__":
    page = connection.open_url("https://www.watchguard.com/wgrd-products/appliances-compare/1320/1320/1320")
    pt = Product('M440', page)
    data = pt.get_product_performance()
    print(pt.name)
    for i in data:
        print(i)