#!/usr/bin/env python
# -*- coding: utf-8 -*-

class foobase:
    def a(self):
        print "hello"

class foo:
    def a(self):
        print "foo"

f = getattr(foobase, "a")
print type(f)
print dir(f)
print f.im_class
print f.im_func
print f.im_self
setattr(foo, "a", f.im_func)  # f.im_func会得到真正的函数对象
c = foo()
c.a()

'''ubuntu@huzhi-dev:~/www/python-patterns$ python mixin_test_03.py 
<type 'instancemethod'>
['__call__', '__class__', '__cmp__', '__delattr__', '__doc__', '__format__', '__func__', '__get__', 
'__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'im_class', 'im_func', 'im_self']
__main__.foobase
<function a at 0x7fdee4102668>
None
hello
ubuntu@huzhi-dev:~/www/python-patterns$ 
'''