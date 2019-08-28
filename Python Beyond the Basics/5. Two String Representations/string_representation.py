# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 09:59:04 2019

@author: Saravanakumar
"""
class Point2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __str__(self):
        return 'String :  x : {x} , y : {y}'.format(x = self._x, y = self._y)
    def __repr__(self):
        return 'Representation : x : {x} , y : {y}'.format(x = self._x, y = self._y)
    
p = Point2D(2,3)
 print(p)