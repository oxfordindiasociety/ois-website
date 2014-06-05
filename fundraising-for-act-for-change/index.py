#!/usr/bin/python
# Sign up form

places = 60
import os
import cgi
import time
import cgitb
import sys
import fundraising
cgitb.enable()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

signuptext = ""

filecount = lambda d: len([name for name in os.listdir(d) if os.path.isfile(os.path.join(d,name))])

sign_up_full = filecount(fundraising.formdir) >= places

if(sign_up_full):
    signuptext = "<p><big>Sign-up closed as we ran out of places. Sorry!</big></p>"
else:
    signuptext = """
    <h3>Sign-up for the dinner</h3>
    <h5><span style="color:green">%d</span> people have signed up!</h5>
<form action="/fundraising-for-act-for-change/signup" method="POST">
  <label for="name">Name</label>
    <input id="name" class="form-control" type="text" name="name">
<br/>
  <label for="email">E-mail</label>
    <input id="email" type="email" class="form-control" name="email">
<br/>
<p><button type="submit" class="btn btn-success">Signup!</button></p>
</form>
""" % filecount(fundraising.formdir)

if time.gmtime() < time.strptime("Mon May 26 18:00:00 2014"):
    signuptext = "<p><big>Sign-up will open on <b>Monday, May 26 at 7pm</b></big></p>."

print fundraising.html % signuptext
