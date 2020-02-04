#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CatalogClass(object):
    """
    test = CatalogClass('param_value_2')
    test.main_method()
    """

    x1 = 'x1'
    x2 = 'x2'

    def __init__(self, param):
        # simple test to validate param value
        if param in self._class_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @classmethod
    def _class_method_1(cls):
        print("Value {}".format(cls.x1))

    @classmethod
    def _class_method_2(cls):
        print("Value {}".format(cls.x2))

    _class_method_choices = {'param_value_1': _class_method_1,
                             'param_value_2': _class_method_2}

    def main_method(self):
        self._class_method_choices[self.param].__get__(None, self.__class__)()


CatalogClass('param_value_1').main_method()
CatalogClass('param_value_2').main_method()
