#!/bin/bash
# get body size with curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
