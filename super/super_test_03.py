#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):
    name = ""
    sex = ""

    def __init__(self, name, sex='U'):
        print 'Person'
        self.name = name
        self.sex = sex


class Consumer(object):
    def __init__(self):
        print 'Consumer'


class Student(Person, Consumer):
    def __init__(self, score, name):
        print Student.__bases__ # (<class '__main__.Person'>, <class '__main__.Consumer'>)
        super(Student, self).__init__(name, sex='F')
        Consumer.__init__(self)
        self.score = score


s1 = Student(90, 'abc')
print s1.name, s1.score, s1.sex

"""
(<class '__main__.Person'>, <class '__main__.Consumer'>)
Person
Consumer
abc 90 F
"""