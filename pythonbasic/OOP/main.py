# -*- coding: utf-8 -*-
from Employee import *

def set_age(self, age):
    self.age = age

if __name__ == "__main__":
    employee = Employee('jaymiao', 100)
    employee.displayCount()
    employee.displayEmployee()

    from types import MethodType
    Employee.set_age = MethodType(set_age, None, Employee)
    # employee.set_age = MethodType(set_age, employee, Employee)
    employee.set_age(23)
    print employee.age


