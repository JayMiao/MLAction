# -*- coding: utf-8 -*-

class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x ** 2

ob = MyObject()
print hasattr(ob, 'x')

setattr(ob,'y', 19)
print getattr(ob, 'y')
