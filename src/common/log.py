# -*- coding:utf-8 -*-
"""
@author: jiangkai
@file:log.py
@time:2018/06/03 12:33:16
"""
import logging
from src.config.default import LOG_FILE_NAME


class Log(object):

    def __init__(self, log_name, level=logging.DEBUG):
        self.log = logging.getLogger(log_name)
        self.log.setLevel(level)
        fmt = logging.Formatter("[%(name)s][%(asctime)s][%(filename)s][%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(level)
        fh = logging.FileHandler(LOG_FILE_NAME)
        fh.setFormatter(fmt)
        fh.setLevel(level)
        self.log.addHandler(sh)
        self.log.addHandler(fh)

    def debug(self, message):
        self.log.debug(message)

    def info(self, message):
        self.log.info(message)

    def warning(self, message):
        self.log.warning(message)

    def error(self, message):
        self.log.error(message)

    def critical(self, message):
        self.log.critical(message)

    def exception(self, message):
        self.log.exception(message)
