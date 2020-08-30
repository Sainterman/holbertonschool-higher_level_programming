#!/usr/bin/python3
"""Check POST request with letter as parameter"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    post = requests.post(url, data=payload)
    try:
        r = post.json()
        if len(r) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r['id'], r['name']))
    except:
        print("Not a valid JSON")
