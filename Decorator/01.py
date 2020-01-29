#! /usr/bin/env python

'''
def now():
    print '2013-12-25'

f = now
f()
# 2013-12-25

print now.__name__ # now

print f.__name__ # now
'''

'''
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log # now = log(now)
def now():
    print '2013-12-25'

now()
# call now():
# 2013-12-25
'''

def log(text):
    def decorator(func):
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

print now.__name__ # wrapper

