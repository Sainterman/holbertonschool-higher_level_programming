#!/usr/bin/python3
"""send POST to url with requests module"""
import sys
import requests


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    payload = {'email': email}
    x = requests.post(url, data=payload)
    print(x.text)
