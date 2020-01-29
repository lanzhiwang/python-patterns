#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    def __init__(self):
        self.__x = 3 # self._A__x

    def __spam(self): # _A__spam
        pass

    def bar(self):
        self.__spam() # 调用 A.__spam()

class B(A):
    def __init__(self):
        A.__init__(self)
        self.__x = 37 # self._B__x

    def __spam(self): # _B__spam
        pass
'''
__dir__() 显示实例的所有属性和方法
dir()
getattr()
hasattr()
setattr()
delattr()

'''


