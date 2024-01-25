#!/bin/bash
# script that takes in a url and displys all HTTP methods
curl -s -X OPTIONS "$1" | grep -o 'Allow:.*' | sed 's/Allow: //'
