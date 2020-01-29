#!/usr/bin/env python
# -*- coding: utf-8 -*-

class WebFramework(object):
    '''所谓描述器，即实现描述符协议的对象，即__get__, __set__, 和 __delete__方法的对象
    descriptor也必须依附对象，作为对象的一个属性，它而不能单独存在
    '''
    def __init__(self, name='Flask'):
        self.name = name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        self.name = value


class PythonSite(object):

    webframework = WebFramework()

print PythonSite.webframework  # Flask

PythonSite.webframework = 'Tornado'
print PythonSite.webframework  # Tornado

f = WebFramework()
print f.name

