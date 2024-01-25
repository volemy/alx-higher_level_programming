#!/usr/bin/bash
# script that sends url passed as first argument and displays response
curl -s -X DELETE "$1" | json_pp
