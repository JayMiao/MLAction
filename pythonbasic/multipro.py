# -*- coding: utf-8 -*-
import os
#
pid = os.fork()
#
# if pid == 0:
#     print os.getpid()
#     print os.getppid()
#
# else:
#     print os.getpid()
#     print pid


from multiprocessing import Process
import os

def run_proc(name):
    print 'child ... %s, pid %s ' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s. ' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print  'Process will start.'
    p.start()
    p.join()
    print 'Process end.'