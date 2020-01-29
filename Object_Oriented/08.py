#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 描述符对象
'''
class TypeProperty(object):
    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        self.default = default if default else type()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

class Foo(object):
    name = TypeProperty("name", str)
    num = TypeProperty("num", int, 42)

f = Foo()
a = f.name # Foo.name.__get__(f, Foo)
f.name = "Guido" # Foo.name.__set__(f, "Guido")
del f.name # Foo.name.__delete__(f)
