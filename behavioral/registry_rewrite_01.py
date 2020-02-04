#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RegistryHolder(type):

    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)  # new_cls = super(RegistryHolder, cls).__new__(cls, name, bases, attrs)
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(metaclass=RegistryHolder):
    # __metaclass__ = RegistryHolder
    pass


if __name__ == "__main__":
    print("Before subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)  # BaseRegisteredClass

    class ClassRegistree(BaseRegisteredClass):

        def __init__(self, *args, **kwargs):
            pass

    print("After subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)
        """
        BaseRegisteredClass
        ClassRegistree
        """
