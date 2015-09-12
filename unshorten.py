#! /usr/bin/python

import sys

try:
    from urllib2 import Request as Request
    from urllib2 import build_opener as build_opener
    from urllib2 import HTTPErrorProcessor as HTTPErrorProcessor
except ImportError as e:
    from urllib.request import Request as Request
    from urllib.request import build_opener as build_opener
    from urllib.request import HTTPErrorProcessor as HTTPErrorProcessor


class NoRedirection(HTTPErrorProcessor):
    def http_response(self, request, response):
        return response

    https_response = http_response


if len(sys.argv) not in (2, 3):
    print('usage: unshorten [-v] <url>')
    sys.exit(1)

if len(sys.argv) == 3:
    verbose = sys.argv[1] == '-v'
else:
    verbose = False

url = sys.argv[-1]
if verbose:
    print(url)

opener = build_opener(NoRedirection())

request = Request(url)
request.get_method = lambda : 'HEAD'
request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0')
response = opener.open(request)

while str(response.code).startswith('3'):
    if verbose:
        print(response.headers['location'])
    
    newurl = response.headers['location']
    request = Request(newurl)
    request.get_method = lambda : 'HEAD'
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0')
    response = opener.open(request)

if not verbose:
    print(response.url)