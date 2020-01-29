#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def follow(thefile, target):
    thefile.seek(0, 2)  # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        target.send(line)


@coroutine
def printer():
    while True:
        line = (yield)
        print line


@coroutine
def grep(pattern, target):
    while True:
        line = (yield)  # Receive a line
        if pattern in line:
            target.send(line)  # Send to next stage


@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)


f = open("access-log")
p = printer()
follow(f,
       broadcast(
           [
               grep('python', p),
               grep('ply', p),
               grep('swig', p)
           ]
                 )
       )














f = open("access-log")
target = grep('python', printer())
follow(f, target)