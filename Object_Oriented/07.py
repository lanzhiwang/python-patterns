#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Circle(object):

    def __init__(self, radius):
        self.radius = radius # 实例变量

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print c.radius
print c.area
print c.perimeter

# c.area = 2 # 错误操作

class Foo(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("Can't delete name")

'''
class Foo(object):
    def __init__(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setname(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        self.__name = value

    def delname(self):
        raise TypeError("Can't delete name")
    
    name = property(getname, setname, delname)
'''


