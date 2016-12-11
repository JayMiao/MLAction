# -*- coding: utf-8 -*-
def deco(func):
    def _deco(*args, **kwargs):
        print "befor call %s" % func.__name__
        ret = func(*args, **kwargs)
        print "after call ret: %s" % ret
        return ret
    return _deco

@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b


@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a + b + c


myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)