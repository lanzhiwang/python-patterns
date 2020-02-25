#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reference:
http://www.slideshare.net/ishraqabd/publish-subscribe-model-overview-13368808
Author: https://github.com/HanWenfang
"""


# 提供者
class Provider:
    """
    message_center = Provider()
    fftv = Publisher(message_center)
    jim = Subscriber("jim", message_center)
    """

    def __init__(self):
        self.msg_queue = []
        self.subscribers = {}

    def notify(self, msg):
        self.msg_queue.append(msg)

    def subscribe(self, msg, subscriber):
        self.subscribers.setdefault(msg, []).append(subscriber)

    def unsubscribe(self, msg, subscriber):
        self.subscribers[msg].remove(subscriber)

    def update(self):
        for msg in self.msg_queue:
            for sub in self.subscribers.get(msg, []):
                sub.run(msg)
        self.msg_queue = []


class Publisher:
    """
    message_center = Provider()
    fftv = Publisher(message_center)
    jim = Subscriber("jim", message_center)
    """

    def __init__(self, msg_center):
        self.provider = msg_center

    def publish(self, msg):
        self.provider.notify(msg)


class Subscriber:
    """
    message_center = Provider()
    fftv = Publisher(message_center)
    jim = Subscriber("jim", message_center)
    jim.subscribe("cartoon")
    """

    def __init__(self, name, msg_center):
        self.name = name
        self.provider = msg_center

    def subscribe(self, msg):
        self.provider.subscribe(msg, self)

    def unsubscribe(self, msg):
        self.provider.unsubscribe(msg, self)

    def run(self, msg):
        print("{} got {}".format(self.name, msg))

    def __repr__(self):
        return 'Subscriber name: %s' % self.name


def main():
    message_center = Provider()
    fftv = Publisher(message_center)

    jim = Subscriber("jim", message_center)
    jim.subscribe("cartoon")

    jack = Subscriber("jack", message_center)
    jack.subscribe("music")

    gee = Subscriber("gee", message_center)
    gee.subscribe("movie")
    gee.subscribe("music")

    vani = Subscriber("vani", message_center)
    vani.subscribe("movie")
    vani.unsubscribe("movie")

    print(message_center.subscribers)
    """
    []
    {
        'cartoon': [Subscriber name: jim],
        'music': [Subscriber name: jack, Subscriber name: gee],
        'movie': [Subscriber name: gee]
    }
    """

    fftv.publish("cartoon")
    fftv.publish("music")
    fftv.publish("ads")
    fftv.publish("movie")
    fftv.publish("cartoon")
    fftv.publish("cartoon")
    fftv.publish("movie")
    fftv.publish("blank")
    print(message_center.msg_queue)
    """
    ['cartoon', 'music', 'ads', 'movie', 'cartoon', 'cartoon', 'movie', 'blank']
    """

    message_center.update()


if __name__ == "__main__":
    main()

### OUTPUT ###
# jim got cartoon
# jack got music
# gee got movie
# jim got cartoon
# jim got cartoon
# gee got movie
