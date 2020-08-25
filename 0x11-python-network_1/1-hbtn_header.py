#!/usr/bin/python3
"""thisjust happens"""

import urllib.request as request
import sys

if __name__ == '__main__':
    with request.urlopen("{}".format(sys.argv[1])) as resp:
        header = resp.info()
        print(header['X-Request-Id'])
