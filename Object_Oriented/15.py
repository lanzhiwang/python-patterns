#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty

class Foo(object):
    __metaclass__ = ABCMeta # 在 Python3 中的写法是 class Foo(metaclass=ABCMeta)

    @abstractmethod
    def spam(self, a, b):
        pass

    @abstractproperty
    def name(self):
        pass

class Grok(object):
    def spam(self, a, b):
        print("Grok.spam")

Foo.register(Grok)
