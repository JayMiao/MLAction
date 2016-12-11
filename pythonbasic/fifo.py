# -*- coding: utf-8 -*-

from collections import OrderedDict

class FIFO(OrderedDict):
    def __init__(self, capacity):
        # super(LastUpdatedOrderedDict, self).__init__()
        OrderedDict.__init__(self)
        self._capacity = capacity

    def __setitem__(self, key, value):
        keyexist = 1 if key in self else 0
        if keyexist == 1:
            OrderedDict.__setitem__(self, key, value)
        else:
            if len(self) + 1 > self._capacity:
                self.popitem(last=False)
                OrderedDict.__setitem__(self, key, value)
            else:
                OrderedDict.__setitem__(self, key, value)

fifo = FIFO(3)
fifo['a'] = 1
fifo['b'] = 1
fifo['c'] = 1
fifo['d'] = 1
print fifo