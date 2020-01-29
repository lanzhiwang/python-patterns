#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DocMeta(type):
    def __init__(self, name, bases, dict):
        for key, value in dict.items():
            # 跳过特殊方法和私有方法
            if key.startswith("__"):
                continue
            # 跳过不可调用的任何方法
            if not hasattr(value, "__call__"):
                continue
            # 检测doc字符串
            if not getattr(value, "__doc__"):
                raise TypeError("%s must have a docstring" % key)
        type.__init__(self, name, bases, dict)

class Documented(object):
    __metaclass__ = DocMeta  # 在 Python3 中的写法是 class Foo(metaclass=DocMeta)

class Foo(Documented):
    def spam(self, a, b):
        "spam does something"
        pass
