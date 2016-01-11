#!/usr/bin/python
from pygelf import GelfTcpHandler, GelfUdpHandler, GelfTlsHandler
import re
import sys
import logging
import os

flag = os.environ['HOME']
print flag

parts = [
    r'(?P<host>\S+)',                   # host %h
    r'(?P<indent>\S+)',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
    r'"(?P<xuid>.*)"'
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

#line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827" "Abc:DEF"'
for line in sys.stdin:
    log_data=[]
    m = pattern.match(line)
    res = m.groupdict()
    logging.info("total number of events parsed: %s" % len(log_data))
    fields = {
        '_remote_host':        res['host'],
        '_remote_user':        res['user'],
        '_request_time':       res['time'],
        '_request_line':       res['request'],
        '_request_status':     res['status'],
        '_request_size':       res['size'],
        '_request_referer':    res['referer'],
        '_request_agent':      res['agent'],
        '_request_xunique_id': res['xuid']
    }
    print res
