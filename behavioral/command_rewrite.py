#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*TL;DR80
Encapsulates all information needed to perform an action or trigger an event.
"""

from __future__ import print_function
import os


class MoveFileCommand(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)

    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):
        os.rename(src, dest)


if __name__ == "__main__":
    cmd = MoveFileCommand('foo.txt', 'bar.txt')
    cmd.execute()
    cmd.undo()
