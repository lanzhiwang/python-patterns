#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


class State(object):

    """Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(u"Scanning... Station is %s %s" %
              (self.stations[self.pos], self.name))


class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print(u"Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print(u"Switching to AM")
        self.radio.state = self.radio.amstate


class Radio(object):
    def __init__(self):
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


# Test our radio out
if __name__ == '__main__':
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    print(actions)
    """
    [
    <bound method Radio.scan of <__main__.Radio object at 0x1021a11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x1021a11d0>>, 
    <bound method Radio.toggle_amfm of <__main__.Radio object at 0x1021a11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x1021a11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x1021a11d0>>
    ]
    """
    actions *= 2
    print(actions)
    """
    [
    <bound method Radio.scan of <__main__.Radio object at 0x105fa11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x105fa11d0>>, 
    <bound method Radio.toggle_amfm of <__main__.Radio object at 0x105fa11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x105fa11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x105fa11d0>>,
     
    <bound method Radio.scan of <__main__.Radio object at 0x105fa11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x105fa11d0>>, 
    <bound method Radio.toggle_amfm of <__main__.Radio object at 0x105fa11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x105fa11d0>>, 
    <bound method Radio.scan of <__main__.Radio object at 0x105fa11d0>>
    ]
    """

    for action in actions:
        action()

### OUTPUT ###
# Scanning... Station is 1380 AM
# Scanning... Station is 1510 AM
# Switching to FM
# Scanning... Station is 89.1 FM
# Scanning... Station is 103.9 FM

# Scanning... Station is 81.3 FM
# Scanning... Station is 89.1 FM
# Switching to AM
# Scanning... Station is 1250 AM
# Scanning... Station is 1380 AM
