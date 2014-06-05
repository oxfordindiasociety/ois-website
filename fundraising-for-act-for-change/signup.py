#!/usr/bin/python
# Sign up form

import os
import cgi
import cgitb
import sys
import fundraising

from uuid import uuid4

cgitb.enable()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

form = cgi.FieldStorage()

# validation

def signup(name, email):
  signuptext = ""
  uid = str(uuid4())
  signup_str = "%s <%s>" % (name.strip(), email.strip())
  with open(os.path.join(fundraising.formdir, uid), "w") as f:
    print >>f, "%s <%s>" % (name.strip(), email.strip())
  signuptext += "<h3>Hi %s, you are signed up for the dinner!</h3>" % name.split()[0]
  signuptext += "<p>You have been signed up as<br><tt>%s</tt>" % cgi.escape(signup_str)
  signuptext += "<p>You'll receive a confirmation email with details of how to pay.</p><p>ticket code<br><tt>%s</tt></p>" % uid
  return signuptext

if "name" not in form or "email" not in form:
  signuptext = "<p><big>Sign-up form was not filled out completely. Please <a href='/fundraising-for-act-for-change/'>return</a> and fill out all the fields.</big></p>"
else:
  signuptext = signup(form["name"].value, form["email"].value)

print fundraising.html % signuptext
