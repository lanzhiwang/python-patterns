#!/usr/bin/env python
# -*- coding: utf-8 -*-

class C(object):

    a = 'abc'

    def __init__(self, name):
        self.name = name

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, name):
        print("__getattr__() is called ")
        return name + " from getattr"

    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)
        return self

    def foo(self, x):
        print(x)


class C2(object):
    d = C('in C2')


if __name__ == '__main__':

    c = C('test')

    print(c.a)
    '''__getattribute__() is called
    abc
    '''
    print '=======================' * 10

    print(c.zzzzzzzz)
    '''__getattribute__() is called
    __getattr__() is called 
    zzzzzzzz from getattr
    '''
    print '=======================' * 10

    print(c.name)
    '''__getattribute__() is called
    test
    '''
    print '=======================' * 10

    print(c.name_other)
    '''__getattribute__() is called
    __getattr__() is called 
    name_other from getattr
    '''
    print '=======================' * 10

    c2 = C2()
    print(c2.d.a)
    '''('__get__() is called', <__main__.C2 object at 0x7fb5448a7090>, <class '__main__.C2'>)
    __getattribute__() is called
    abc
    '''
    print '=======================' * 10