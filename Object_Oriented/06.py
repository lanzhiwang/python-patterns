#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 类方法
    @classmethod
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_day)

    # 类方法
    @classmethod
    def tomorrow(cls):
        t = time.localtime(time.time() + 86400)
        return cls(t.tm_year, t.tm_mon, t.tm_day)

class EuroDate(Date):
    pass

a = Date.now() # 返回 Date 对象
b = EuroDate.now() # 返回 EuroDate 对象
