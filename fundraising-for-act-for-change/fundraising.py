#!/usr/bin/python
# Sign up form common data

formdir = "/ois/fundraising-2014-june/"
html = """
<!doctype html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Oxford India Society - Fundraising for Act for Change India</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css" />
<link rel="stylesheet" type="text/css" href="/css/style.css" />
<script src="/js/jquery-1.11.1.js"></script>
<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
  <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
<![endif]-->
<script src="/js/bootstrap.min.js"></script>
</head>
<body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Oxford India Society</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li><a href="/about">About</a></li>
            <li><a href="/events">Events</a></li>
            <li><a href="/press">Press</a></li>
            <li><a href="http://policyblog.oxfordindiasociety.org.uk">Policy Blog</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container main">

        <h2>Fundraising for the Act for Change India</h2>

    <div class="alert alert-info">
    <p style="font-family:Raleway,sans-serif;font-weight:bold">The event is at <strong>Corpus Christi College</strong>, Merton Road
    <span class="glyphicon glyphicon-time"></span> 6 - 9.30pm
    </div>

          <div class="row">
  
    <div class="col-sm-6 col-md-4">
    <div class="thumbnail">
    <img src="vegbiriyani.jpg">
    </div>
    <p>
    Oxford India Society is hosting a <b>fundraiser for <a href="https://www.facebook.com/actforchangein">Act for Change India</a></b>
    in the form of a dinner get together on <b>7th June 2014</b>. Act for Change India is an initiative to
    spread mental health awareness in India through forum theatre.</p>
    <p>
    In an endeavour to support their cause, OIS has planned an evening where we
   will have some of the best amongst us enact their talents ranging from
   theatre, music to maybe even a bit of magic. The dinner will be prepared by
   our student volunteers and we promise a meal that would taste, smell and
   feel like home.</p>
   <p>The money raised during this event would be used to support  street plays
and theatre performances across India as a part of this mental health
awareness campaign.</p>
  <p><b>Performances will be from 6 - 7pm and dinner will be from 7 - 9.30pm</b></p>

   </div>


  <div class="col-sm-6 col-md-4">
          <div class="thumbnail">
    <img src="aloogobi.jpg">
    </div>


  <h3>Menu</h3>
  <dl>
  <dt>Starters</dt>
    <dd>Masala papad</dd>
  <dt>Mains</dt>
    <dd>Veg Biryani, Daal Makhani, Aloo Gobi</dd>
    <dd>Naan bread</dd>
  <dt>Dessert</dt>
  <dd>Cake</dd>
  </dl>

  <p><b>Price is 5 GBP per person.</b></p>

<p>We hope you will join us and support our endeavour to contribute to the
mental health awareness campaign in India.</p>
  </div>

    <div class="col-sm-6 col-md-4">
              <div class="thumbnail">
    <img src="daalmakhani.jpg">
    </div>

    %s
    </div>

        </div>
  <div class="footer">
  <p>Veg Biryani photo from http://tastyappetite.net<br>
  Aloo Gobi photo by Paul Goyette https://secure.flickr.com/photos/pgoyette/339987980/<br>
  Daal Makhani photo by Charles Haynes https://secure.flickr.com/photos/haynes/1547098753/
  </div>


    </div><!-- /.container -->

</body>
</html>
"""

