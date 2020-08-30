#!/usr/bin/python3
"""Fetch using requests module"""
import requests

if __name__ == "__main__":
    x = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(x.text)))
    print("\t- content: {}".format(x.text))
