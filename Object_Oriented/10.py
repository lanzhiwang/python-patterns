#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

# 创建实例的方法一
# c = Circle(4.0)
c = Circle.__new__(Circle, 4.0)
if isinstance(c, Circle):
    Circle.__init__(c, 4.0)

# 创建实例的方法二
d = Circle(5.0)

# __new__(cls, *args, **kwargs)

class Upperstr(str):
    def __new__(cls, value=""):
        return str.__new__(cls, value.upper())

u = Upperstr("hello") # 值为 HELLO

'''
__del__()

del obj

'''