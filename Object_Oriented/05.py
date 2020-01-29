#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Foo(object):

    # 静态方法
    @staticmethod
    def add(x, y):
        return x + y

x = Foo.add(3, 4)

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 静态方法
    @staticmethod
    def now():
        t = time.localtime()
        return Data(t.tm_year, t.tm_mon, t.tm_day)

    # 静态方法
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Data(t.tm_year, t.tm_mon, t.tm_day)

a = Date(1967, 4, 9)
b = Date.now()
c = Date.tomorrow()

a.now()

class Times(object):
    factor = 1

    # 类方法
    @classmethod
    def mul(cls, x):
        return cls.factor * x

class TwoTimes(Times):
    factor = 2

x = TwoTimes.mul(4) # Times.mul(TwoTimes, 4)
