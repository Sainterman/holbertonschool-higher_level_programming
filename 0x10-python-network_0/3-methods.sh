#!/bin/bash
# take url and display all HTTP methods the server will accept
curl -sI "$1" | grep -i Allow | awk '{print substr($0, index($0,$2))}'
