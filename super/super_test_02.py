#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
总之前人留下的经验就是：保持一致性。要不全部用类名调用父类，要不就全部用 super，不要一半一半
"""

"""
新式类
新式类，要求最顶层的父类一定要继承于object
"""

class A(object):
    def __init__(self):
        print 'A'

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print 'B'

class C(B, A):
    def __init__(self):
        super(C, self).__init__()
        print 'C'

"""
C先继承A，再继承B，会出现错误
class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print 'C'
"""

a = A()
"""
A
"""

b = B()
"""
A
B
"""

c = C()
"""
A
B
C
"""


