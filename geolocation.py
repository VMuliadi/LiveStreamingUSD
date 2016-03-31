from urllib.request import urlopen
from bs4 import BeautifulSoup
latitude = input('Latitude :: ')
longitude = input('Longitude :: ')
api_key = '';
page = urlopen('https://maps.googleapis.com/maps/api/geocode/json?latlng='+latitude+','+longitude+'&'+api_key+'')
