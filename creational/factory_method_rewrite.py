#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GreekGetter(object):
    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()


if __name__ == '__main__':
    e = get_localizer(language="English")
    g = get_localizer(language="Greek")
    for msgid in ['dog', 'parrot', 'cat', 'bear']:
        print(e.get(msgid), g.get(msgid))
    """
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """
