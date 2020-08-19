#!/bin/bash
# sends a request to a URL passed as an argumen t,and displays only the status
curl -s -o /dev/null -w %{http_code} "$1"
