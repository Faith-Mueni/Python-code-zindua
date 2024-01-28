import requests
from bs4 import BeautifulSoup

import csv

url = "https://hojaleaks.com"

response = requests.get (url)

soup = BeautifulSoup (response.content, "html.parser")

headings = soup.find_all ("h1", class_ ='blog-article-card-title')

#print(headings)

for heading in headings:
    #print (heading.text)

    images = soup.find_all("img")

for image in images:
    #print (images['src'])

    read_times = soup.find_all ('span', class_= "flex items-center")
    print (time.text)
