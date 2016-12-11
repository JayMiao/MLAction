# -*- coding: utf-8 -*-
array = [1,2,3,4,5,6]

def sum_1(num):
    return num+1

# print map(sum_1, array)


def add(a, b):
    return a+b

print reduce(add, array)

def big(a):
    return a > 3

print filter(big, array)