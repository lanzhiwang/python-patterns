#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""经典类"""

class A():
    def __init__(self):
        print 'A'

class B(A):
    def __init__(self):
        A.__init__(self)
        print 'B'

class C(B, A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print 'C'


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
A
B
C
"""

