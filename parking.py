from bs4 import BeautifulSoup
import urllib.request 

html_file = urllib.request.urlopen("https://parkingapps.ucr.edu/spaces/")

soup = BeautifulSoup(html_file, 'html.parser')

print(soup.prettify())