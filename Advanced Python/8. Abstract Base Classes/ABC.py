# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:33:56 2019

@author: Saravanakumar
"""

class SwordMetal(type):
    
    def __isinstancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    
    def __subclasscheck__(cls, sub):
        return (hasattr(sub, 'swipe') and callable(sub.swipe) 
                and 
                hasattr(sub, 'sharpen') and callable(sub.sharpen))
    
class Sword(metaclass = SwordMetal):
    pass

class BroadSword:
    def swipe(self):
        print('swipe')
        
    def sharpen(self):
        print('sharpen')
    

class SamuraiSword:
    def swipe(self):
        print('swipe')
        
    def sharpen(self):
        print('sharpen')
        
class Riffle:
    
    def fire():
        print('fire')
        
        
print(issubclass(BroadSword, Sword))
print(issubclass(SamuraiSword, Sword))
r= Riffle()
print(isinstance(r, Sword))
b = BroadSword()
print(isinstance(b, Sword))