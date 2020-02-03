#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weakref


class FlyweightMeta(type):
    print('解释器会扫描到这里')
    def __new__(mcs, name, parents, dct):
        print('mcs: %s' % mcs)
        print('name: %s' % name)
        # print('parents: %s' % parents)
        print('dct: %s' % dct)
        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
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


def with_metaclass(meta, *bases):
    """
    with_metaclass(FlyweightMeta)
    return FlyweightMeta("NewBase", bases, {})
    """
    print('解释器不会扫描到这里')
    temp = meta("NewBase", bases, {})
    print('构建了一个 FlyweightMeta 实例')
    return temp


class Card2(with_metaclass(FlyweightMeta)):
    """
    Card2 = Card2(FlyweightMeta("NewBase", bases, {}))
    """
    print('构建 Card2 对象本身')
    def __init__(self, *args, **kwargs):
        print('in Card2 init')


print(isinstance(Card2, FlyweightMeta))

"""
huzhi@huzhideMacBook-Pro structural % python3 flyweight_rewrite_04.py
解释器会扫描到这里
解释器不会扫描到这里
mcs: <class '__main__.FlyweightMeta'>
name: NewBase
dct: {}
构建了一个 FlyweightMeta 实例
构建 Card2 对象本身
mcs: <class '__main__.FlyweightMeta'>
name: Card2
dct: {'__module__': '__main__', '__qualname__': 'Card2', '__doc__': '\n    Card2 = Card2(FlyweightMeta("NewBase", bases, {}))\n    ', '__init__': <function Card2.__init__ at 0x105bc58c8>}
True
huzhi@huzhideMacBook-Pro structural %
"""