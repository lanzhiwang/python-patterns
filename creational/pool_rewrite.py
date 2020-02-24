#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ObjectPool(object):

    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        print('__enter__')
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        print('__exit__')
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        print('__del__')
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    try:
        import queue
    except ImportError:
        import Queue as queue

    sample_queue = queue.Queue()

    sample_queue.put('yam')
    op = ObjectPool(sample_queue)
    with op as obj:
        print('Inside with: {}'.format(obj))  # Inside with: yam

    with op as obj:
        print('Inside with: {}'.format(obj))  # Inside with: yam

    print('Outside with: {}'.format(sample_queue.get()))  # Outside with: yam

    def test_object(queue):
        pool = ObjectPool(queue, True)
        print('Inside func: {}'.format(pool.item))  # Inside func: sam

    sample_queue.put('sam')
    test_object(sample_queue)
    print('Outside func: {}'.format(sample_queue.get()))  # Outside func: sam

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == '__main__':
    main()

"""
__enter__
Inside with: yam
__exit__
__enter__
Inside with: yam
__exit__
Outside with: yam
Inside func: sam
__del__
Outside func: sam
__del__
"""