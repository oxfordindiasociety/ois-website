#!/usr/bin/python
# Sign up form

import os
import cgi
import cgitb
import sys
import email
import email.mime.text
import smtplib
import fundraising

from uuid import uuid4

cgitb.enable()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

form = cgi.FieldStorage()

# validation
fromaddr = "Oxford Indian Society <indian.society@studentclubs.ox.ac.uk>"
textmail = """Dear %s,

This is the confirmation that you have signed up for:

    Fundraising for the Act for Change
    organised by the Oxford India Society

    at Corpus Christi College Dining Hall
    on Saturday, 7 June, 6 - 9.30pm

    ticket #%s

Please bring 5 GBP to pay at the door.

Hope to see you there!

Regards
Team OIS
"""
def msg(val, uuid):
    name, e = email.utils.parseaddr(val)
    m = email.mime.text.MIMEText(textmail % (name.split()[0], uuid))
    m['Subject'] = "Signup confirmation: Fundraising for Act for Change"
    m['From'] = fromaddr
    m['To'] = val
    return m

def signup(name, email):
  signuptext = ""
  uid = str(uuid4())
  signup_str = "%s <%s>" % (name.strip(), email.strip())
  with open(os.path.join(fundraising.formdir, uid), "w") as f:
    print >>f, "%s <%s>" % (name.strip(), email.strip())
  signuptext += "<h3>Hi %s, you are signed up for the dinner!</h3>" % name.split()[0]
  signuptext += "<p>You have been signed up as<br><tt>%s</tt>" % cgi.escape(signup_str)
  signuptext += "<p>You'll receive a confirmation email with details of how to pay.</p><p>ticket code<br><tt>%s</tt></p>" % uid
  return signuptext, uid

if "name" not in form or "email" not in form:
  signuptext = "<p><big>Sign-up form was not filled out completely. Please <a href='/fundraising-for-act-for-change/'>return</a> and fill out all the fields.</big></p>"
else:
  signuptext, uid = signup(form["name"].value, form["email"].value)
  s = smtplib.SMTP('localhost')
  s.sendmail(fromaddr, [form["email"].value.strip()], msg(form["name"].value.strip() + " <" + form["email"].value.strip() + ">", uid).as_string())
  s.quit()

print fundraising.html % signuptext

