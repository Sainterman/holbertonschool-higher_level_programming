#!/bin/bash
# sends a json as post
curl -s "$1" -d @"$2" -H "Content-Type: application/json"
