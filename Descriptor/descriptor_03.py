#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Descriptor(object):

    '''
    self 指的是当前 Descriptor 的实例
    obj  指的是拥有属性的对象，这里的 obj 就是拥有它的对象
    type 指的是obj的类型

    ps : 如果是直接实例化 Descriptor，obj == None， type==Descriptor

    descr.__get__(self, obj, type=None) --> value
    descr.__set__(self, obj, value) --> None
    descr.__delete__(self, obj) --> None
    '''
    def __get__(self, obj, type=None):
            return 'get', self, obj, type

    def __set__(self, obj, val):
        print 'set', self, obj, val

    def __delete__(self, obj):
        print 'delete', self, obj

class T(object):
    d = Descriptor()
t = T()


'''查找属性时，如obj.attr，如果Python发现这个属性attr有个__get__方法，
Python会调用attr的__get__方法，返回__get__方法的返回值，
而不是返回attr
'''

'''
1、descriptor必须依附对象，作为对象的一个属性，它不能单独存在
2、descriptor必须存在于类的 __dict__ 中，这句话的意思是只有在类的__dict__中找到属性，Python才会去看看它有没有__get__等方法，
对一个在实例的__dict__中找到的属性，Python根本不理会它有没有__get__等方法，直接返回属性本身
3、descriptor是对象的一个属性，只不过它存在于类的__dict__中并且有特殊方法__get__(可能还有__set__和__delete__)
'''

'''
读取属性
t.d，返回的是d.__get__(t, T)的结果
T.d，返回的是d.__get__(None, T)的结果

设置属性
t.d = value，实际上调用d.__set__(t, value)
T.d = value，这是真正的赋值，T.d的值从此变成value

删除属性
del t.d
del T.d
'''

print t.d # ('get', <__main__.Descriptor object at 0x7f617980b450>, <__main__.T object at 0x7f617971be90>, <class '__main__.T'>)
print T.d # ('get', <__main__.Descriptor object at 0x7f617980b450>, None, <class '__main__.T'>)


t.d = 'hello' # set <__main__.Descriptor object at 0x7f51ec3fe450> <__main__.T object at 0x7f51ec30ee90> hello
print t.d # ('get', <__main__.Descriptor object at 0x7f617980b450>, <__main__.T object at 0x7f617971be90>, <class '__main__.T'>)
print T.d # ('get', <__main__.Descriptor object at 0x7f617980b450>, None, <class '__main__.T'>)

T.d = 'hello' #
print t.d # hello
print T.d # hello


# del t.d
# del t.d
