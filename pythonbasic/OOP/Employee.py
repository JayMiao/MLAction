# -*- coding: utf-8 -*-
class Employee(object):
    empCount = 0
    __slots__ = ('name', 'salary')
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total employ count is %d " % (self.empCount)

    def displayEmployee(self):
        print "Name: %s Salay: %d" % (self.name, self.salary)
