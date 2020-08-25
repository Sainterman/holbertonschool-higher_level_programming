#!/usr/bin/python3
"""thisjust happens"""

import urllib.request as request
import sys

with request.urlopen("{}".format(sys.argv[1])) as resp:
    header = resp.info()
    print(header['X-Request-Id'])
