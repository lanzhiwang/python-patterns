#! /usr/bin/env python

'''
import functools

def log(func):
    @functools.wraps(func) # wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
'''


import functools

def log(text):
    def decorator(func):
        @functools.wraps(func) # # wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute') # now = log('execute')(now)
def now(data):
    print data

now('2013-12-25')
# execute now():
# 2013-12-25

print now.__name__ # now

