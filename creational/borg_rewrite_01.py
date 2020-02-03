#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Borg(object):

    shared_state = {}

    def __init__(self):
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    print(rm1)  # Init
    print(rm1.__dict__)  # {'state': 'Init'}
    print(Borg.shared_state)  # {}

    print("=" * 20)

    rm2 = Borg()
    print(rm2)  # Init
    print(rm2.__dict__)  # {'state': 'Init'}
    print(Borg.shared_state)  # {}

    print("=" * 20)

    rm1.state = 'Idle'
    print(rm1)  # Idle
    print(rm1.__dict__)  # {'state': 'Idle'}
    print(Borg.shared_state)  # {}

    print("=" * 20)

    rm2.state = 'Running'

    print(rm2)  # Running
    print(rm2.__dict__)  # {'state': 'Running'}
    print(Borg.shared_state)  # {}

    print("=" * 20)

    print('rm1: {0}'.format(rm1))  # rm1: Idle
    print('rm2: {0}'.format(rm2))  # rm2: Running

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))  # rm1: Idle
    print('rm2: {0}'.format(rm2))  # rm2: Zombie

    print('rm1 id: {0}'.format(id(rm1)))  # rm1 id: 140702079541328
    print('rm2 id: {0}'.format(id(rm2)))  # rm2 id: 140702079541456

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))  # rm1: Idle
    print('rm2: {0}'.format(rm2))  # rm2: Zombie
    print('rm3: {0}'.format(rm3))  # rm3: Init
