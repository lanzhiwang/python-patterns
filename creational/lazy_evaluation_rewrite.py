#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import functools


class lazy_property(object):
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


def lazy_property2(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)
    return _lazy_property


class Person(object):
    """
    john = Person('john', 'Coder')
    print(john.name, john.occupation)  # john Coder
    """
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    """
    relatives = lazy_property(relatives)
    """
    @lazy_property
    def relatives(self):
        relatives = "Many relatives."
        return relatives

    """
    parents = lazy_property2(parents)
    """
    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    john = Person('john', 'Coder')
    print(john.name, john.occupation)  # john Coder

    print(u"Before we access `relatives`:")
    print(john.__dict__)  # {'name': 'john', 'occupation': 'Coder', 'call_count2': 0}

    print(john.relatives)  # Many relatives

    print(u"After we've accessed `relatives`:")
    print(john.__dict__)  # {'name': 'john', 'occupation': 'Coder', 'call_count2': 0, 'relatives': 'Many relatives.'}

    print(john.parents)  # Father and mother

    print(john.__dict__)  # {'name': 'john', 'occupation': 'Coder', 'call_count2': 1, 'relatives': 'Many relatives.', '_lazy__parents': 'Father and mother'}

    print(john.parents)  # Father and mother
    print(john.call_count2)  # 1


if __name__ == '__main__':
    main()
