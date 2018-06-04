# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:control.py
@time:2018/06/04 08:00:45
"""
from threading import Thread
from src.config.default import USER_PRODUCT
from src.framework.view.visual import Visual
from src.framework.model.watchguard import WatchGuard


class Control(WatchGuard):

    def __init__(self, user_product):
        super(Control, self).__init__(user_product)
        self.product_obj_list = []

    def save_performance_data(self):
        """
            @summary 存储产品的performance数据
        :return:
        """
        self.save_product_obj()
        # 遍历每个产品对象，获取所以的产品数据存以列表形式放在all_data中
        all_data = []
        for probj in self.product_obj_list:
            pf = probj.get_product_performance()
            all_data.append(pf)
        # 对all_data中的字典按照键值 Firewall Throughput 进行升排序,
        # 因为Firewall Throughput单位全部换算成以K为单位的数字，对应键值flag_number,
        # 所以这里以flag_number排序.
        all_data.sort(key=lambda x: x['flag_number'], reverse=False)
        title = []
        value = []
        for i, data in enumerate(all_data):
            temp = []
            for k, v in data.items():
                if not k == "flag_number":
                    if i == 0:
                        title.append(k)
                    temp.append(v)
            value.append(temp)
        # 调用view层进行写文件
        file_name = "..\\..\\data\\performance.csv"
        visual = Visual(file_name)
        visual.write_to_csv(title, value)

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
    ct.save_performance_data()
