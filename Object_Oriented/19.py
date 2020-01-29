#!/usr/bin/env python
# -*- coding: utf-8 -*-

registry = {}
def register(cls):
    registry[cls.__clsid__] = cls
    return cls

@register
class Foo(object):
    __clsid__ = "123-456"
    def bar(self):
        pass

'''
class Foo(object):
    __clsid__ = "123-456"
    def bar(self):
        pass
register(Foo) # 注册类
'''
