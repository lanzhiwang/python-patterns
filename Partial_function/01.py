#! /usr/bin/env python

'''
print int('12345') # 12345

print int('12345', base=8) # 5349

print int('12345', 16) # 74565

def int2(x, base=2):
    return int(x, base)

print int2('1000000') # 64
print int2('1010101') # 85
'''

import functools
int2 = functools.partial(int, base=2)
'''
kw = { base: 2 }
int('10010', **kw)
'''
print int2('1000000') # 64
print int2('1010101') # 85
print int2('1000000', base=10) # 1000000

max2 = functools.partial(max, 10)
print max2(5, 6, 7) # 10
# args = (10, 5, 6, 7)
# max(*args)
