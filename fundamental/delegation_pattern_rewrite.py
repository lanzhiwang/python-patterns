#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Delegator(object):
    """
    >>> delegator = Delegator(Delegate())
    >>> delegator.do_something("nothing")
    'Doing nothing'
    >>> delegator.do_anything()

    """

    def __init__(self, delegate):
        self.delegate = delegate

    def __getattr__(self, name):
        print(name)
        """
        do_something
        do_anything
        """
        def wrapper(*args, **kwargs):
            if hasattr(self.delegate, name):
                attr = getattr(self.delegate, name)
                if callable(attr):
                    return attr(*args, **kwargs)
        return wrapper


class Delegate(object):

    def do_something(self, something):
        return "Doing %s" % something


if __name__ == '__main__':
    delegator = Delegator(Delegate())
    print(delegator.do_something("nothing"))
    print(delegator.do_anything())
