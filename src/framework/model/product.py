# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:product.py
@time:2018/06/03 23:50:38
"""
from bs4 import BeautifulSoup
from src.config.default import PERFORMANCE
from src.common import convert
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
        :return performance_data: 返回一个字典(key：性能名称，value：性能数据)
        """
        short_name = str(self.name).split(' ')[-1]
        performance_data = {"Model": short_name}
        flag_number = 0
        for tr in self.tr_tag:
            td = tr.find_all('td')
            for index, v in enumerate(td):
                title = str(v.text).strip()
                if index < td.__len__()-1:
                    value = str(td[index + 1].text).strip()
                if title and title in PERFORMANCE:
                    if title == 'Firewall Throughput':
                        flag_number = convert.data_flow(value)
                    performance_data.update({title: value})
        performance_data.update({'flag_number': flag_number})
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
    print(pt.get_product_performance())