#!/usr/bin/python3
"""some times its hard"""

import urllib.request as request


with request.urlopen("https://intranet.hbtn.io/status") as resp:
    data = resp.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(data), data, data.decode("utf-8")))
