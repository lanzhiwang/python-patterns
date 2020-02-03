#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.

*What does this example do?
To understand the implementation of this pattern in Python, it is
important to know that, in Python, instance attributes are stored in a
attribute dictionary called __dict__. Usually, each instance will have
its own dictionary, but the Borg pattern modifies this so that all
instances have the same dictionary.
In this example, the __shared_state attribute will be the dictionary
shared between all instances, and this is ensured by assigining
__shared_state to the __dict__ variable when initializing a new
instance (i.e., in the __init__ method). Other attributes are usually
added to the instance's attribute dictionary, but, since the attribute
dictionary itself is shared (which is __shared_state), all other
attributes will also be shared.
For this reason, when the attribute self.state is modified using
instance rm2, the value of self.state in instance rm1 also chages. The
same happends if self.state is modified using rm3, which is an
instance from a subclass.
Notice that even though they share attributes, the instances are not
the same, as seen by their ids.

"""


class Borg(object):

    shared_state = {}

    def __init__(self):
        self.__dict__ = self.shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    print(rm1)  # Init
    print(rm1.__dict__)  # {'state': 'Init'}
    print(Borg.shared_state)  # {'state': 'Init'}

    print("=" * 20)

    rm2 = Borg()
    print(rm2)  # Init
    print(rm2.__dict__)  # {'state': 'Init'}
    print(Borg.shared_state)  # {'state': 'Init'}

    print("=" * 20)

    rm1.state = 'Idle'
    print(rm1)  # Idle
    print(rm1.__dict__)  # {'state': 'Idle'}
    print(Borg.shared_state)  # {'state': 'Idle'}

    print("=" * 20)

    rm2.state = 'Running'

    print(rm2)  # Running
    print(rm2.__dict__)  # {'state': 'Running'}
    print(Borg.shared_state)  # {'state': 'Running'}

    print("=" * 20)

    print('rm1: {0}'.format(rm1))  # rm1: Running
    print('rm2: {0}'.format(rm2))  # rm2: Running

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))  # rm1: Zombie
    print('rm2: {0}'.format(rm2))  # rm2: Zombie

    print('rm1 id: {0}'.format(id(rm1)))  # rm1 id: 140702079541328
    print('rm2 id: {0}'.format(id(rm2)))  # rm2 id: 140702079541456

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))  # rm1: Init
    print('rm2: {0}'.format(rm2))  # rm2: Init
    print('rm3: {0}'.format(rm3))  # rm3: Init