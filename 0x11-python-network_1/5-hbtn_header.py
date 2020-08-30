#!/usr/bin/python3
"""get headers with requests module"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    x = requests.get(url)
    if 'X-Request-Id' in x.headers:
        print(x.headers['X-Request-Id'])
