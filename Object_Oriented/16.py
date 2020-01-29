#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Foo(object):
    pass

print isinstance(Foo, object) # true

print type(Foo) # <type 'type'>

# 类名
class_name = "Foo"

# 基类
class_parents = (object, )

# 类主体
class_body = """
def __init__(self, x):
    self.x = x
def blah(self):
    print("hello world!")
"""

class_dict = { }

# 在局部字典 class_dict 中执行类主体
exec(class_body, globals(), class_dict)

# 创建类对象 Foo
Foo = type(class_name, class_parents, class_dict)

