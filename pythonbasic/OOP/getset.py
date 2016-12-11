# -*- coding: utf-8 -*-

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


miao = Student()
miao.birth = 2000
print miao.age