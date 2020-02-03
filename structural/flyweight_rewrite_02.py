#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weakref


class FlyweightMeta(type):
    print('解释器会扫描到这里')
    def __new__(mcs, name, parents, dct):
        print('mcs: %s' % mcs)
        print('name: %s' % name)
        print('parents: %s' % parents)
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

"""
huzhi@huzhideMacBook-Pro structural % python3 flyweight_rewrite_02.py
解释器会扫描到这里
huzhi@huzhideMacBook-Pro structural %
"""