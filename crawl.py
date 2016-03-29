# Vinsen Muliadi - admin@max-metal.us
# https://github.com/MaX121/LiveStreamingUSD/

# importing basic library
import os, sys, subprocess
from urllib.request import urlopen
from bs4 import BeautifulSoup

# first, the program will mark the pwd as the variable
# user input the YouTube link to embed on the webpage
# if the user insert without 'https', automatically add it
basedir = subprocess.check_output('pwd').decode(encoding='UTF-8')
link = input('YouTube Link :: ')
if (link.startswith("youtube.com")) :
    link = "https://" + link

print('Processing Link ...')
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
berkas = open("/var/www/index.html", "w")
berkas.write("<!doctype html>")
berkas.write("<html>")
berkas.write("<head>")
berkas.write("<title>Proyek Teknologi Informasi - Live Streaming Wisuda</title>")
berkas.write("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css' />")
berkas.write("<style type='text/css'>@import url(https://fonts.googleapis.com/css?family=Open+Sans);</style>")
berkas.write("<script type='text/javascript' src='http://code.jquery.com/jquery-1.12.2.min.js'></script>")
berkas.write("<script type='text/javascript' src='"+basedir+"/script.js'></script>")
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
berkas.write("<div class='col-xs-6'>This site is created by PTI - 2016</div>")
berkas.write("<div class='col-xs-3'>Jumlah Tayang :: " + views + "</div>")
berkas.write("<div class='col-xs-3'>Total Pemasukan :: <span id='income'></span> </div>")
berkas.write("</div>")
berkas.write("</div>")
berkas.write("</body>")
berkas.write("<script src='"+basedir+"/editable.js'></script>")
berkas.write("</html>")
berkas.close()

# generating done
print('File generate successfully on /var/www/index.html')
sys.exit(0)
