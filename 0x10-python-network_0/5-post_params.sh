#!/bin/bash
# script that takes in URL sends a POST
curl -s -X POST -d "email=test@gmail.com&subject=i will alwys be here for PLD" "$1"
