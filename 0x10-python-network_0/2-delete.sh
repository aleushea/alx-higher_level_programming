#!/bin/bash
# This script sends a DELETE request to a URL passed as a first argument and displays the response
curl -s "$1" -X DELETE
