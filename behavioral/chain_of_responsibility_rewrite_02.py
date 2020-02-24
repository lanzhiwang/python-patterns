#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import os
import sys
import time


def coroutine1(target):
    while True:
        request = yield
        if 0 < request <= 10:
            print('request {} handled in coroutine 1'.format(request))
        else:
            target.send(request)


def coroutine2():
    while True:
        request = yield
        if 10 < request <= 20:
            print('request {} handled in coroutine 2'.format(request))
        else:
            print('end')



if __name__ == '__main__':
    client1 = coroutine1(coroutine2())
    # client.__next__()
    next(client1)
    client1.send(2)
    """
    request 2 handled in coroutine 1
    """

    client2 = coroutine1(coroutine2())
    # client.__next__()
    next(client2)
    client2.send(15)  # 协程 coroutine2 需要预激
    """
    Traceback (most recent call last):
    File "chain_of_responsibility_rewrite_02_test.py", line 50, in <module>
        client2.send(15)
    File "chain_of_responsibility_rewrite_02_test.py", line 25, in coroutine1
        target.send(request)
    TypeError: can't send non-None value to a just-started generator
    """
