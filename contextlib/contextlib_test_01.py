#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    f = open('/path/to/file', 'r')
    f.read()
finally:
    if f:
        f.close()

with open('/path/to/file', 'r') as f:
    f.read()


