#!/bin/bash
#  Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -s -X GET 0.0.0.:5000/catchme > dev/null
