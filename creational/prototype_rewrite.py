#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Prototype(object):
    """
    prototype = Prototype()
    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    """

    value = 'default'

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    """
    dispatcher = PrototypeDispatcher()
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    """

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]


def main():
    prototype = Prototype()
    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)

    dispatcher = PrototypeDispatcher()
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)

    print([{n: p.value} for n, p in dispatcher.get_objects().items()])
    # [{'objecta': 'a-value'}, {'objectb': 'b-value'}, {'default': 'default'}]


if __name__ == '__main__':
    main()
