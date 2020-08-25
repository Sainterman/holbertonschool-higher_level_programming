#!/usr/bin/python3
"""some times its hard"""

from urllib import request

if __name__== "__main__":
    with(request.urlopen("https://intranet.hbtn.io/status")) as resp:
         data = resp.read()
         print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
               .format(str(type(data)), str(data), str(data.decode("UTF-8"))))
