#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


def count_to(count):
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number

# Test the generator
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)

print('Counting to two...')
for number in count_to_two():
    print(number, end=' ')

print()

print('Counting to five...')
for number in count_to_five():
    print(number, end=' ')

print()

### OUTPUT ###
# Counting to two...
# one two
# Counting to five...
# one two three four five
