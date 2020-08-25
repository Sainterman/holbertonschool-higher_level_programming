#!/usr/bin/python3
"""police man in the fields. are searching mariguana"""
import sys
import urllib.request as request
import urllib.parse as parse

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email})
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
