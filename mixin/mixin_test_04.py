#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BaseClass(object):
    pass

class Mixin1(object):
    def test(self):
        print "Mixin1"

class Mixin2(object):
    def test(self):
        print "Mixin2"

class MyClass1(BaseClass, Mixin1, Mixin2):
    pass

class MyClass2(BaseClass, Mixin2, Mixin1):
    pass


obj1 = MyClass1()
obj1.test()  # Mixin1

obj2 = MyClass2()
obj2.test()  # Mixin2

'''ubuntu@huzhi-dev:~/www/python-patterns$ python mixin_test_04.py 
Mixin1
Mixin2
ubuntu@huzhi-dev:~/www/python-patterns$ 
'''