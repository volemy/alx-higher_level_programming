#!/bin/bash
# script that takes in a url and displys all HTTP methods
curl -s -X OPTIONS "$1" | awk -F ': ' '/Allow:/{print $2}'
