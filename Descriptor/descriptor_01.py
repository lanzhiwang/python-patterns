#!/usr/bin/env python
# -*- coding: utf-8 -*-

class T(object):
    name = 'name'

    def __init__(self, age):
        self.age = age

    def hello(self):
        print 'hello'

t = T(12)

# 使用dir(t)列出t的所有有效属性
# 属性可以分为两类，一类是Python自动产生的，如__class__，__hash__等，
# 另一类是我们自定义的，如上面的hello，name。我们只关心自定义属性。
print dir(t)
'''['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', 
'__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'age', 'hello', 'name']
'''

'''实例对象的 __dict__ 属性'''
print dict(t.__dict__)
'''{'age': 12}
'''

'''类的 __dict__ 属性'''
print dict(T.__dict__)
'''
{'__module__': '__main__', 
'name': 'name', 
'__doc__': None, 
'__dict__': <attribute '__dict__' of 'T' objects>, 
'__weakref__': <attribute '__weakref__' of 'T' objects>, 
'hello': <function hello at 0x7f3dc049b758>, 
'__init__': <function __init__ at 0x7f3dc049b6e0>}
'''