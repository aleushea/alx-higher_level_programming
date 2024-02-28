#!/bin/bash
# This script takes in a URL, sends a GET request to it, and display only body of a 200 status code response
curl -s "$1" -X GET -L
