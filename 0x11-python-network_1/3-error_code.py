#!/usr/bin/python3
"""This Python script takes a URL as a command-line argument, sends a request to that URL, and displays the body of the response (decoded in UTF-8)."""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            url_res = response.read()
            print(url_res.decode('utf-8'))

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
