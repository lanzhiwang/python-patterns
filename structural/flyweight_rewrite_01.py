#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weakref


class Card(object):
    _CardPool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


if __name__ == '__main__':
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1)  # <Card: 9h>
    print(c2)  # <Card: 9h>
    print(c1 == c2, c1 is c2)  # (True, True)
    print(id(c1), id(c2))  # (140386419454288, 140386419454288)

    c1.temp = None
    c3 = Card('9', 'h')
    print(c3, id(c3))  # (<Card: 9h>, 140386419454288)
    print(hasattr(c3, 'temp'))  # True

    c1 = c2 = c3 = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))  # False
