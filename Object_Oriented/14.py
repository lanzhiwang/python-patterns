#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    pass

class B(A):
    pass

class C(object):
    pass

a = A()
b = B()
c = C()

print type(a) # <class '__main__.A'>

print isinstance(a, A) # True
print isinstance(b, A) # True
print isinstance(b, C) # False

print issubclass(B, A) # True
print issubclass(C, A) # False

class Foo(object):
    def spam(self, a, b):
        pass

class FooProxy(object):
    def __init__(self, f):
        self.f = f

    def spam(self, a, b):
        return self.f.spam(a, b)

'''
f = Foo()
g = FooProxy(f)
print isinstance(g, Foo) # False
'''

class IClass(object):
    def __init__(self):
        self.implementors = set()

    def register(self, C):
        self.implementors.add(C)

    def __instancecheck__(self, x):
        return self.__subclasscheck__(type(x))

    def __subclasscheck__(self, sub):
        return any(c in self.implementors for c in sub.mro())

IFoo = IClass()
IFoo.register(Foo)
IFoo.register(FooProxy)

f = Foo()
g = FooProxy(f)

print isinstance(g, IFoo) # True
print isinstance(g, IFoo) # True
print issubclass(FooProxy, IFoo) # True
