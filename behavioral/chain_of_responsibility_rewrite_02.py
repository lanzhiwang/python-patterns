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
def coroutine2(target):
    while True:
        request = yield
        if 10 < request <= 20:
            print('request {} handled in coroutine 2'.format(request))
        else:
            target.send(request)


@coroutine
def coroutine3(target):
    while True:
        request = yield
        if 20 < request <= 30:
            print('request {} handled in coroutine 3'.format(request))
        else:
            target.send(request)


@coroutine
def default_coroutine():
    while True:
        request = yield
        print('end of chain, no coroutine for {}'.format(request))


class ClientCoroutine(object):
    """
    client = ClientCoroutine()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    client.delegate(requests)
    """

    def __init__(self):
        self.target = coroutine1(
            coroutine3(
                coroutine2(
                    default_coroutine()
                )
            )
        )

    def delegate(self, requests):
        for request in requests:
            self.target.send(request)


if __name__ == '__main__':
    client = ClientCoroutine()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    client.delegate(requests)
    """
    request 2 handled in coroutine 1
    request 5 handled in coroutine 1
    request 14 handled in coroutine 2
    request 22 handled in coroutine 3
    request 18 handled in coroutine 2
    request 3 handled in coroutine 1
    end of chain, no coroutine for 35
    request 27 handled in coroutine 3
    request 20 handled in coroutine 2
    """
