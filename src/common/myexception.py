# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:myexception.py
@time:2018/06/03 16:54:24
"""


class MyException(Exception):

    def __init__(self, message):
        super(MyException, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class RequestHostFailed(MyException):

    def __init__(self, message):
        super(RequestHostFailed, self).__init__(message)
