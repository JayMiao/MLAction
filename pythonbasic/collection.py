# -*- coding: utf-8 -*-
from collections import namedtuple

websites = [
    ('Sohu', 'sohu.com', u'zhangchaoyang'),
    ('sina', 'sina.com', u'wangzhidong'),
    ('163', '163.com', u'dinglei'),
]

WebSite = namedtuple('auteman', ['name','url','founder'])

# for website in websites:
#     website = WebSite._make(website)
#     print website

import sys
import time
from collections import deque

fancy_loading = deque('>---------------')

while True:
    print '\r%s' % ''.join(fancy_loading)
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)

