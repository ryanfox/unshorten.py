# unshorten.py #
## A pure-Python command-line url unshortener ##

Obfuscated urls got you down?  Not going to click on some shady link?  Want to find out where it goes, quickly?  Feed it to unshorten.
Note: this isn't secure.  So if you were hoping https would hide the post-host part of the URL, you're out of luck here.

### Usage ###
unshorten [-v] url

If you specify verbose mode, it prints any intermediate redirects.  Try it with [https://goo.gl/hnpGjq](https://goo.gl/hnpGjq) (should redirect to the GitHub repo).

### Requirements ###
Only that Python is installed, and on your path.  Should run on 2 and 3.

### Installation ###
1. Make it executable. `$ chmod u+x unshorten.py`
2. Move it to some place on your path, like `/usr/local/bin/` or `~/bin`.  Try `$ mv unshorten.py /usr/local/bin/unshorten`.
3. That's it.  There is no step 3.

### License ###
The MIT License (MIT)

Copyright (c) 2015 Ryan Fox

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
