#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Account(object):
    '''
    Account类成员 Account.__dict__

    Account.num_accounts
    Account.__init__
    Account.__del__
    Account.deposit
    Account.withdraw
    Account.inquiry
    '''

    # 类变量，在所有实例之间共享
    num_accounts = 0

    # name, balance 实例属性或简称为属性或者实例变量
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    # 类实例方法
    def deposit(self, amt):
        self.balance = self.balance + amt

    # 类实例方法
    def withdraw(self, amt):
        self.balance = self.balance - amt

    # 类实例方法
    def inquiry(self):
        return self.balance

a = Account("Guido", 1000.00) # 调用 Account.__init__(a, "Guido", 1000.00)
b = Account("Bill", 10.00)

a.deposit(100.00)
b.withdraw(50.00)
name = a.name

print Account.num_accounts
# print a.num_accounts

class Foo(object):
    def bar(self):
        print("bar!")

    def spam(self):
        # bar(self) 错误调用方式
        self.bar() # 正确
        Foo.bar(self) # 正确

