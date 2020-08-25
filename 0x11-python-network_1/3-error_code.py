#!/usr/bin/python3
"""error codes"""

import sys
import urllib.request as request
import urllib.error

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
