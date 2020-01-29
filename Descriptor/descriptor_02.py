#!/usr/bin/env python
# -*- coding: utf-8 -*-

class T(object):
    name = 'name'

    def __init__(self, age):
        self.age = age

    def hello(self):
        print 'hello'

t = T(12)

print T.name # name
print T.__dict__['name'] # name
print T.hello # <unbound method T.hello>  # 类是type的实例
print T.__dict__['hello'] # <function hello at 0x7f40945846e0>

print '========' * 10

print t.name # name
#print t.__dict__['name']
'''Traceback (most recent call last):
  File "descriptor_02.py", line 23, in <module>
    print t.__dict__['name']
KeyError: 'name'
'''

print t.hello # <bound method T.hello of <__main__.T object at 0x7f4ea52c5e90>>
print t.__dict__['hello']
'''Traceback (most recent call last):
  File "descriptor_02.py", line 31, in <module>
    print t.__dict__['hello']
KeyError: 'hello'
'''
