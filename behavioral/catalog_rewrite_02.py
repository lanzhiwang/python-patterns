#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CatalogInstance(object):
    """
    test = CatalogInstance('param_value_1')
    test.main_method()
    """
    def __init__(self, param):
        self.x1 = 'x1'
        self.x2 = 'x2'
        # print(self._instance_method_choices)
        """
        {
            'param_value_1': <function CatalogInstance._instance_method_1 at 0x1074362f0>,
            'param_value_2': <function CatalogInstance._instance_method_2 at 0x107436378>
        }
        """
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    def _instance_method_1(self):
        print("Value {}".format(self.x1))

    def _instance_method_2(self):
        print("Value {}".format(self.x2))

    _instance_method_choices = {'param_value_1': _instance_method_1,
                                'param_value_2': _instance_method_2}

    def main_method(self):
        # print(self._instance_method_choices[self.param])
        """
        <function CatalogInstance._instance_method_1 at 0x1056472f0>
        """
        # print(self._instance_method_choices[self.param].__get__(self))
        """
        <bound method CatalogInstance._instance_method_1 of <__main__.CatalogInstance object at 0x10f7305f8>>
        """
        self._instance_method_choices[self.param].__get__(self)()


CatalogInstance('param_value_1').main_method()
CatalogInstance('param_value_2').main_method()
