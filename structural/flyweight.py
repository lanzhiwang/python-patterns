#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*References:
http://codesnipers.com/?q=python-flyweights

*TL;DR80
Minimizes memory usage by sharing data with other similar objects.
"""

import weakref


class FlyweightMeta(type):
    #         meta("NewBase", bases, {})
    def __new__(mcs, name, parents, dct):
        """
        Set up object pool

        :param name: class name
        :param parents: class parents
        :param dct: dict: includes class attributes, class methods,
        static methods, etc
        :return: new class
        """
        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """
        Serialize input parameters to a key.
        Simple implementation is just to serialize it as a string
        """
        args_list = list(map(str, args))
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if instance is None:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance
        return instance


class Card(object):

    """The object pool. Has builtin reference counting"""
    _CardPool = weakref.WeakValueDictionary()

    """Flyweight implementation. If the object exists in the
    pool just return it (instead of creating a new one)"""
    # C.__new__(self[, arg1, ...]) 构造函数（附带任何可选参数）；通常用于创建不可变数据类型的子类
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    # C.__repr__(self) 可计算字符串表示； repr()内置方法和″ 操作符
    # repr(obj) 一种可以计算的字符串表示
    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


def with_metaclass(meta, *bases):
    """ Provide python cross-version metaclass compatibility. """
    return meta("NewBase", bases, {})


class Card2(with_metaclass(FlyweightMeta)):

    def __init__(self, *args, **kwargs):
        # print('Init {}: {}'.format(self.__class__, (args, kwargs)))
        pass


if __name__ == '__main__':
    # comment __new__ and uncomment __init__ to see the difference
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1) # <Card: 9h>
    print(c2) # <Card: 9h>
    print(c1 == c2, c1 is c2) # (True, True)
    print(id(c1), id(c2)) # (140386419454288, 140386419454288)

    c1.temp = None
    c3 = Card('9', 'h')
    print(c3, id(c3)) # (<Card: 9h>, 140386419454288)
    print(hasattr(c3, 'temp')) # True
    c1 = c2 = c3 = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp')) # False

    # Tests with metaclass
    # getattr(object, name[, default])
    # Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.
    instances_pool = getattr(Card2, 'pool')
    print(instances_pool) # <WeakValueDictionary at 139653312150560>
    cm1 = Card2('10', 'h', a=1)
    cm2 = Card2('10', 'h', a=1)
    cm3 = Card2('10', 'h', a=2)

    assert (cm1 == cm2) != cm3
    assert (cm1 is cm2) is not cm3
    assert len(instances_pool) == 2

    del cm1
    assert len(instances_pool) == 2

    del cm2
    assert len(instances_pool) == 1

    del cm3
    assert len(instances_pool) == 0

### OUTPUT ###
# (<Card: 9h>, <Card: 9h>)
# (True, True)
# (31903856, 31903856)
# True
# False
