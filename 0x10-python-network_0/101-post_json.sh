#!/bin/bash
# sends a json as post
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
