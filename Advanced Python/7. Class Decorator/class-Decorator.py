# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:47:18 2019

@author: Saravanakumar
"""
import functools

def check(predicate):
    def check_class_decorator(cls):
        methods_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in methods_names:
            check_method_proxy(cls, name, predicate)
        return cls
    return check_class_decorator

def check_method_proxy(cls, name, predicate):
    method = getattr(cls, name)
    assert callable(method)
    
    @functools.wraps(method)
    def check_method_decorator(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not predicate(self):
            raise RuntimeError('class invarient {!r} violated for {!r}'.format(predicate.__doc__, self))
        return result
    setattr(cls, name, check_method_decorator)


def check_zero(temperature):
    return temperature._kelvin >=0
        
@check(check_zero)
class Temperature:
    
    def __init__(self, kelvin):
        self._kelvin = kelvin
        
    def get_kelvin(self):
        return self._kelvin
    
    def set_kelvin(self, value):
        self._kelvin = value
        
t = Temperature(23)
t = Temperature(-23)