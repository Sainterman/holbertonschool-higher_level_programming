#!/usr/bin/python3
"""error codes"""

import sys
import urllib.request as request


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
