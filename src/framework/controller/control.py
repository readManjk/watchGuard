# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:control.py
@time:2018/06/04 08:00:45
"""
from threading import Thread
from src.config.default import USER_PRODUCT
from src.framework.model.watchguard import WatchGuard


class Control(WatchGuard):

    def __init__(self, user_product):
        super(Control, self).__init__(user_product)
        self.product_obj_list = []

    def save_performance(self):
        """
            @summary 存储产品的performance数据
        :return:
        """
        self.save_product_obj()
        for probj in self.product_obj_list:
            probj.get_product_performance()
            print(1)
            break

    def save_product_obj(self):
        """
            @summary 采用多线程获取存储产品对象【如果产品数量过多，则要限制多线程，防止服务器忙于过多请求，
                     具体限制数量根据网站性能和要求给出】
        :return:
        """
        user_prd = self.choose_product()
        thread_list = []
        for prd in user_prd:
            name = prd['name']
            pid = prd['id']
            self.thread_action(name, pid)
            th = Thread(target=self.thread_action, args=(name, pid))
            thread_list.append(th)
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join(60)

    def thread_action(self, name, pid):
        prd = self.get_product_obj(name, pid)
        self.product_obj_list.append(prd)


if __name__ == '__main__':
    ct = Control(USER_PRODUCT)
    ct.save_performance()