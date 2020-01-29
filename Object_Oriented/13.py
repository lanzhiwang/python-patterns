#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Complex(object):
    def __init__(self, real, imag=0):
        self.real = float(real)
        self.imag = float(imag)

    def __repr__(self): # 用于直接输出实例
        return "Complex(%s,%s)" % (self.real, self.imag)

    def __str__(self): # 用于 print
        return "(%g+%g)" % (self.real, self.imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other):
        return Complex(other.real + self.real, other.imag + self.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        return Complex(other.real - self.real, other.imag - self.imag)

c = Complex(2, 3)
c + 4.0



