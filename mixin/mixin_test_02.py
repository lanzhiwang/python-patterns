#!/usr/bin/env python
# -*- coding: utf-8 -*-

class fooase:
    def a(self):
        print "foobase"

class foo(foobase):
    def a(self):
        print "foo"

c = foo()
c.a()
'''ubuntu@huzhi-dev:~/www/python-patterns$ python mixin_test_02.py 
foo
ubuntu@huzhi-dev:~/www/python-patterns$ 
'''

'''在基类与派生类中都有同名的函数，要如何处理呢？
在Python中，如果派生类中有与基类同名的函数，那么调用函数时，会调用派生类的函数，而不是基类的函数
'''




