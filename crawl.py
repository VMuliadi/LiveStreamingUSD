import os, sys, re
from urllib.request import urlopen
from bs4 import BeautifulSoup
link = input('YouTube Link :: ')
print('Processing Link ...')

# validating URL that inputted by user
# require internet connection
if (link.startswith("youtube.com")) :
    link = "https://" + link

page = urlopen(link)

# get the YouTube video ID
# the link started with https://
videoID = link.replace(link[:32], '')

# get the div.watch-view-count value
print('Generating index.html')
bsoup = BeautifulSoup(page, "lxml")
views = bsoup.find("div", {'class' : 'watch-view-count'}).prettify()

# creating index.html
# if the file already exist, Python will replace it with the new one
berkas = open("index.html", "w")
berkas.write("<!doctype html>")
berkas.write("<html>")
berkas.write("<head>")
berkas.write("<title>Proyek Teknologi Informasi - Live Streaming Wisuda</title>")
berkas.write("<link rel='stylesheet' href='bootstrap_3.3.4/css/bootstrap.min.css' />")
berkas.write("<style type='text/css'>@import url(https://fonts.googleapis.com/css?family=Open+Sans);</style>")
berkas.write("<script type='text/javascript' src='http://code.jquery.com/jquery-1.12.2.min.js'></script>")
berkas.write("<script type='text/javascript' src='script.js'></script>")
berkas.write("</head>")
berkas.write("<body>")
berkas.write("<div class='container-fluid'>")
berkas.write("<div class='row'>")
berkas.write("<div class='col-xs-12'>")
berkas.write("<div align='center'><iframe id='youtube-video' src='https://www.youtube.com/embed/" + videoID + "?rel=0&autoplay=1' frameborder='0' allowfullscreen></iframe></div>")
berkas.write("</div>")
berkas.write("</div>")
berkas.write("</div>")
berkas.write("<div class='container-fluid' id='menubar-bottom'>")
berkas.write("<div class='row'>")
# berkas.write("<div class='col-xs-12'>This site is created by PTI - 2016 | This watched " + views + " times with fee y IDR</div>")
berkas.write("<div class='col-xs-6'>This site is created by PTI - 2016</div>")
berkas.write("<div class='col-xs-3'>Jumlah Tayang :: " + views + "</div>")
berkas.write("<div class='col-xs-3'>Total Pemasukan :: <span id='income'></span> </div>")
berkas.write("</div>")
berkas.write("</div>")
berkas.write("</body>")
berkas.write("<script src='editable.js'></script>")
berkas.write("</html>")
berkas.close()
print('File generate successfully')

# generating done
print('File ready on index.html at ' + os.path.dirname(os.path.realpath('index.html')))
sys.exit(0)
