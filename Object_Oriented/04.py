#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Account(object):
    '''
    Account类成员

    Account.num_accounts
    Account.__init__
    Account.__del__
    Account.deposit
    Account.withdraw
    Account.inquiry
    '''

    # 类变量，在所有实例之间共享
    num_accounts = 0

    # name, balance 实例属性或简称为属性
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

class EvilAccount(Account):

    def __init__(self, name, balance, evilfactor):
        Account.__init__(self, name, balance)
        self.evilfactor = evilfactor

    # 类实例方法
    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * self.evilfactor
        else:
            return self.balance

class MoreEvilAccount(EvilAccount):

    # 类实例方法
    def deposit(self, amount):
        self.withdraw(5.00)
        # EvilAccount.deposit(self, amount)
        super(MoreEvilAccount, self).deposit(amount) # super(cls, instance)
        # super().deposit(amount) # python3 调用方式


class DepositCharge(Account):
    fee = 5.00

    def deposit_fee(self):
        # self.withdraw(self.fee)
        self.withdraw(DepositCharge.fee)


class WithdrawCharge(Account):
    fee = 2.50

    def withdraw_fee(self):
        # self.withdraw(self.fee)
        self.withdraw(WithdrawCharge.fee)


class MostEvilAccount(EvilAccount, DepositCharge, WithdrawCharge):
    # 类实例方法
    def deposit(self, amt):
        self.deposit_fee()
        super(MostEvilAccount, self).deposit(amt)

    # 类实例方法
    def withdraw(self, amt):
        self.withdraw_fee()
        super(MostEvilAccount, self).withdraw(amt)


a = Account("Guido", 1000.00) # 调用 Account.__init__(a, "Guido", 1000.00)

b = Account("Bill", 10.00)

c = EvilAccount("George", 1000.00, 1.10)
c.deposit(10.0)
available = c.inquiry()

d = MostEvilAccount("Dave", 500.00, 1.10)
d.deposit_fee()
d.withdraw_fee()

print MostEvilAccount.__mro__


