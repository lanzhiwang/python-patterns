#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 描述符对象
'''
class TypeProperty(object):
    def __init__(self, type, default=None):
        self.name = None
        self.type = type
        if default:
            self.default = default
        else:
            self.default = type()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

class TypedMeta(type):
    def __new__(cls, name, bases, dict):
        slots = []
        for key, value in dict.items():
            if isinstance(value, TypeProperty):
                value.name = "_" + key
                slots.append(value.name)
        dict['__slots__'] = slots
        return type.__new__(cls, name, bases, dict)

class Typed(object):
    __metaclass__ = TypedMeta  # 在 Python3 中的写法是 class Foo(metaclass=TypedMeta)

class Foo(Typed):
    name = TypeProperty(str)
    num = TypeProperty(int, 42)

f = Foo()
a = f.name # Foo.name.__get__(f, Foo)
f.name = "Guido" # Foo.name.__set__(f, "Guido")
del f.name # Foo.name.__delete__(f)



