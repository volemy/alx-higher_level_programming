#!/bin/bash
#  takes $ sends a GET request to URL, then displays body of the response
curl -s -X GET -i "$1" | awk '/HTTP\/1.1 200 OK/{p=1} p' | tail -n +2
