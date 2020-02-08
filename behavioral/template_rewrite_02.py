#!/usr/bin/env python
# -*- coding: utf-8 -*-

ingredients = "spam eggs apple"
line = '-' * 10


# Skeletons
def iter_elements(getter, action):
    """Template skeleton that iterates items"""
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order"""
    for element in getter()[::-1]:
        action(element)
        print(line)


# Getters
def get_list():
    return ingredients.split()


def get_lists():
    return [list(x) for x in ingredients.split()]


# Actions
def print_item(item):
    print(item)


def reverse_item(item):
    print(item[::-1])


# Makes templates
def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""
    def template():
        skeleton(getter, action)
    return template

# Create our template functions
templates = [make_template(s, g, a)
             for s in (iter_elements, rev_elements)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)]

# Execute them
for template in templates:
    template()
    print('*' * 20)

"""
spam
----------
eggs
----------
apple
----------
********************
maps
----------
sgge
----------
elppa
----------
********************
['s', 'p', 'a', 'm']
----------
['e', 'g', 'g', 's']
----------
['a', 'p', 'p', 'l', 'e']
----------
********************
['m', 'a', 'p', 's']
----------
['s', 'g', 'g', 'e']
----------
['e', 'l', 'p', 'p', 'a']
----------
********************
apple
----------
eggs
----------
spam
----------
********************
elppa
----------
sgge
----------
maps
----------
********************
['a', 'p', 'p', 'l', 'e']
----------
['e', 'g', 'g', 's']
----------
['s', 'p', 'a', 'm']
----------
********************
['e', 'l', 'p', 'p', 'a']
----------
['s', 'g', 'g', 'e']
----------
['m', 'a', 'p', 's']
----------
********************
"""
