# -*- coding: utf-8 -*-

class animal(object):
    def run(self):
        print 'im running ...'

class Dog(animal):
    pass

class Cat(animal):
    pass

dog = Dog()
dog.run()
cat = Cat()
cat.run()
