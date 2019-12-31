# -*- coding: utf-8 -*-
import os
import writegridcode_captions

bodyFixed = """ <!-- Bootstrap -->

<body>
<nav class="navbar navbar-default " role = "navigation">
		<div class="container-fluid container">
				<!-- Brand and toggle get grouped for better mobile display -->
				<div class="navbar-header">
						<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#defaultNavbar1"><span id="mobileMenu" class="white"> Menu </span> <span class="glyphicon glyphicon-chevron-down white"></span> </button>
						<a class="navbar-brand" href="http://thedesignerd.in"><img src="/images/brand.svg" alt="" id="navbrand"></a></div>
				<!-- Collect the nav links, forms, and other content for toggling -->
				<div class="collapse navbar-collapse" id="defaultNavbar1">
						<ul class="nav navbar-nav">
								<li><a href="/index.html"><img src="/images/home-icon.svg" alt="">Home</a></li>
								<li><a href="/work.html"><img src="/images/work-icon.svg" alt="">Work</a></li>
								<li><a href="/photos.html"><img src="/images/photos-icon.svg" alt="">Photos</a></li>
								<li><a href="/designs.html"><img src="/images/designs-icon.svg" alt="">Designs</a></li>
								<li><a href="/meandus.html"><img src="/images/meandus-icon.svg" alt="">Me and Us</a></li>
								<li><a href="/blog.html"><img src="/images/blog-icon.svg" alt="">Blog</a></li>
						</ul>
				</div>
				<!-- /.navbar-collapse -->
		</div>
		<!-- /.container-fluid -->
</nav>
<div class="container"> """

def headerBuilder(description, keywords, title):
    header = []
    header.append('<head>')
    header.append('<meta charset="UTF-8">')
    header.append('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
    header.append('<meta name= "description" content="'+ description +'">')
    header.append('<meta name="author" content="Dipan Ghosh">')
    header.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    header.append('<meta name="keywords" content="'+ keywords +'">')
    header.append('<link rel="icon" type="image/png" href="/images/favicon.ico">')
    header.append('<title>' + title + ' </title>')
    header.append("""<link href="/css/bootstrap.css" rel="stylesheet">
<!-- Custom CSS -->
<link rel="stylesheet" href="/css/custom.css" type="text/css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ekko-lightbox/5.1.1/ekko-lightbox.min.css">

<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>""")
    return '\n'.join(header)

def descriptionMaker(title, description):
    desc = []
    desc.append('<section>')
    desc.append('<h2>' + title +'</h2>')
    desc.append('<p>' + description + '</p>')
    desc.append('<p>Have a look </p>')
    desc.append('</section>')
    desc.append('<div class="imagegrid">')
    return '\n'.join(desc)

#imageGrid = writegridcode_captions.imageGridCode()

divCloser = '</div></div>'

footer = """<footer class="row container-fluid">
		<div class="container">
				<figure class="text-center col-md-offset-0 col-md-3"> <img src="/images/brand-footer.svg" alt="" id="footerbrand"> </figure>
				<div class="text-center col-md-offset-0 col-md-3 footercontact col-lg-5">
						<div class="text-center row"> <a href="https://www.facebook.com/dipan.ghosh.10" class="sb facebook">Facebook</a> <a href="https://twitter.com/ThisisDipan" class="sb twitter">Twitter</a> <a href="https://plus.google.com/+DipanGhosh" class="sb google">Linkedin</a> <a href="https://www.youtube.com/channel/UCuVznyH32OZUQZnJrYxAwFw" class="sb youtube">Youtube</a> <a href="https://www.linkedin.com/in/dipan-ghosh-17842257/https://www.linkedin.com/in/dipan-ghosh-17842257/" class="sb linkedin">LinkedIn</a> </div>
						<a href="/contact.php" class="white">
<button class="btn btn-info text-center" id = "contactbtn">
						Contact me
						</button></a>
				</div>
				<div class="text-center col-md-offset-0 col-md-3 col-lg-1">
						<a href="/sitemap.html" ><button class="btn btn-default" id="sitemapbtn">
						Sitemap
						</button></a>
				</div>
				<nav class="text-center col-md-offset-0 col-md-3">
						<ul class="row" id="footermenulist">
								<li class="col-md-3 white footermenu"><a href="/index.html">Home</a></li>
								<li class="col-md-3 white footermenu"><a href="/work.html">Work</a></li>
								<li class="col-md-3 white footermenu"><a href="/photos.html">Photos</a></li>
								<li class="col-md-3 white footermenu"><a href="/designs.html">Designs</a></li>
								<li class="col-md-3 white footermenu"><a href="/meandus.html">Me and Us</a></li>
								<li class="col-md-3 white footermenu"><a href="/blog.html">Blog</a></li>
						</ul>
				</nav>
				
		</div>
		<div class="text-center col-md-offset-0 col-md-12 black">
				<p class="small grey">© 2017 Dipan Ghosh ALL RIGHTS RESERVED </p>
		</div>
</footer>
<!-- jQuery (necessary for Bootstrap's JavaScript plugins) --> 
<script src="/js/jquery-1.11.3.min.js"></script> 
<!-- Include all compiled plugins (below), or include individual files as needed --> 
<script src="/js/bootstrap.js"></script> 
<!-- SVGeezy fallback for SVGs being used--> 
<script src="/js/svgeezy.min.js"></script>
<script src="/js/ekko-lightbox.js"></script>
<script src="/js/imageshow.js"></script> 
<script>svgeezy.init('nocheck', 'png');</script>
<!-- Google Analyics Tracking code--> 
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-91898116-1', 'auto');
  ga('send', 'pageview');

</script>
</body>
</html>
"""



class galleryPage():
    path = ''
    title = ''
    description = ''
    keywords = ''
    def setinfo(self, title, desc, keyw):
        self.title = title
        self.description = desc
        self.keywords = keyw
    def createPage(self):
        page = []
        page.append('<!DOCTYPE html> <html lang="en">')
        page.append(headerBuilder(self.description, self.keywords, self.title))
        page.append(bodyFixed)
        page.append(descriptionMaker(self.title, self.description))
        page.append(writegridcode_captions.imageGridCode(self.path, self.title))
        page.append(divCloser)
        page.append(footer)
        return page

