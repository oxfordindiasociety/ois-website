#!/usr/bin/python
# Sign up form

import os
import cgi
import cgitb
import sys
cgitb.enable()

print "Content-Type: text/plain"     # HTML is following
print                               # blank line, end of headers

formdir = "/ois/fundraising-2014-june/"
files = os.listdir(formdir)

l = []
for fn in files:
  with open(os.path.join(formdir, fn)) as f: l.append(f.readline()[:-1])
print ",\n".join(l)
