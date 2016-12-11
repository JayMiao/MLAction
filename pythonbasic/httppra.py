# -*- coding: utf-8 -*-
import httplib
conn = httplib.HTTPConnection('www.baidu.com')
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.status