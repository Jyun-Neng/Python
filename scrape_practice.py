import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_loc='
loc = 'Taipei'
page = '0'

url = base_url + loc + '&start=' + page

yelp_r = requests.get(url) # Get the source code of this url.

print(yelp_r.status_code) # if status code is 200, it means the page is OK.

yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser') # Get the html format.
#print(yelp_soup.prettify()) # Show the html format.

for link in yelp_soup.findAll("a"): # Find the lines which first word is a.
	print(link)