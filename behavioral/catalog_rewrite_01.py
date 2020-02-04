#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Catalog(object):
    """
    >>> Catalog('param_value_1').main_method()
    executed method 1!
    >>> Catalog('param_value_2').main_method()
    executed method 2!
    """
    def __init__(self, param):
        self._static_method_choices = {'param_value_1': self._static_method_1,
                                       'param_value_2': self._static_method_2}

        if param in self._static_method_choices.keys():
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("executed method 1!")

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    def main_method(self):
        self._static_method_choices[self.param]()


Catalog('param_value_1').main_method()
Catalog('param_value_2').main_method()
