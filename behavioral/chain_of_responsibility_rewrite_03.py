#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import os
import sys
import time


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


@coroutine
def coroutine1(target):
    while True:
        request = yield
        if 0 < request <= 10:
            print('request {} handled in coroutine 1'.format(request))
        else:
            target.send(request)


@coroutine
def coroutine2():
    while True:
        request = yield
        if 10 < request <= 20:
            print('request {} handled in coroutine 2'.format(request))
        else:
            print('end')


if __name__ == '__main__':
    print(coroutine1)  # <function coroutine.<locals>.start at 0x106ee52f0>
    client1 = coroutine1(coroutine2())
    print(client1)  # <generator object coroutine1 at 0x1058a7660>
    client1.send(2)
    """
    request 2 handled in coroutine 1
    """

    client2 = coroutine1(coroutine2())
    client2.send(15)
    """
    request 15 handled in coroutine 2
    """
