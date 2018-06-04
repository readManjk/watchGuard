# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:watchguard.py
@time:2018/06/03 23:23:38
"""
from bs4 import BeautifulSoup
from src.config.default import COMPARE_URL, USER_PRODUCT
from src.framework.model import connection
from src.framework.model.product import Product


class WatchGuard(object):

    def __init__(self, user_product):
        self.compare_url = COMPARE_URL
        self.user_product = user_product

    def choose_product(self):
        """
            @summary  获取指定的产品列表
        :return: data: [list] ，返回一个列表，其中元素是字典包含设备name和id
        """
        data = []
        page_text = connection.open_url(self.compare_url)
        soup = BeautifulSoup(page_text, 'lxml')
        select_tag = soup.find_all('select', attrs={'name': 'p1'})[0]
        optgroup = select_tag.find_all('optgroup')
        # 遍历下拉框选择Firebox M Series、Firebox T Series型号的设备id
        for group in optgroup:
            label = str(group.get('label'))
            if label in self.user_product:
                # 获取到该型号的option标签列表
                option_list = group.find_all('option')
                for opt in option_list:
                    name = str(opt.text)
                    value = str(opt.get('value'))
                    data.append({'name': name, 'id': value})
        return data

    def get_product_obj(self, name, pid):
        """
            获取产品对象
        :return: Product 对象
        """
        url = COMPARE_URL + "/%s/%s/%s" % (pid, pid, pid)
        page = connection.open_url(url)
        prd = Product(name, page)
        return prd
