#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CatalogStatic(object):
    """
    test = CatalogStatic('param_value_1')
    test.main_method()
    """

    def __init__(self, param):
        # simple test to validate param value
        # print(self._static_method_choices)
        """
        {
            'param_value_1': <staticmethod object at 0x10cc60240>,
            'param_value_2': <staticmethod object at 0x10cc60278>
        }
        """
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("executed method 1!")

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    _static_method_choices = {'param_value_1': _static_method_1,
                              'param_value_2': _static_method_2}

    def main_method(self):
        """will execute either _static_method_1 or _static_method_2

        depending on self.param value
        """
        # print(self._static_method_choices[self.param])
        """
        <staticmethod object at 0x1077bd240>
        """
        # print(self._static_method_choices[self.param].__get__(None, self.__class__))
        """
        <function CatalogStatic._static_method_1 at 0x1077c52f0>
        """
        self._static_method_choices[self.param].__get__(None, self.__class__)()


CatalogStatic('param_value_1').main_method()
CatalogStatic('param_value_2').main_method()
