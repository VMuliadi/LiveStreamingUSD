import os
import sys
import requests
from bs4 import BeautifulSoup
from jinja2 import FileSystemLoader, Environment

with open('counter.txt','w') as counter:
	counter.write('0')  # Generate counter

# Generate watch.php to Load the YouTube Video
current_directory = os.path.dirname(os.path.abspath(__file__))
jinja2_env = Environment(loader = FileSystemLoader(current_directory))
web_template = jinja2_env.get_template('watch_template.template')
with open('watch.php','w') as watch: 
	youtube_code = sys.argv[1].split('/')[-1].replace('watch?v=','')
	watch.write(web_template.render(youtube_code = youtube_code)
