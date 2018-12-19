from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()