#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weakref # 弱引用模块

class Account(object):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.observers = set()

    def __del__(self):
        for ob in self.observers:
            ob.close()
        del self.observers

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for ob in self.observers:
            ob.update()

    def withdraw(self, amt):
        self.balance = self.balance - amt
        self.notify()

class AccountObserver(object):
    def __init__(self, theaccount):
        self.theaccount = theaccount
        theaccount.register(self)

    def __del__(self):
        self.theaccount.unregister(self)
        del self.theaccount

    def update(self):
        print("Balance is %0.2f" % self.theaccount.balance)

    def close(self):
        print("Account no longer in use")

a = Account('Dave', 1000.00)
a_ob = AccountObserver(a)

print a.__dict__ # 显示实例的属性值
print a.__class__
print a.__bases__

print Account.__dict__.keys()
print Account.__bases__

'''
obj.name = value -> obj.__setattr__("name", value)
del obj.name -> obj.__delattr__("name")
obj.name -> obj.__getattribute__("name") -> obj.__getattr__()

'''


