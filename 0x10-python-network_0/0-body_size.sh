#!/bin/bash
# this script takes in a URL, it sends it, and displays the size
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
