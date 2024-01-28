#a tool used to get data from the web.. 
# you use two libraries. 1. request library- allows  us to send HTTP requests. 2. Beautiful soup
#pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.nytimes.com/"

response = requests.get (url)

#print (response.content)

soup = BeautifulSoup (response.content, 'html.parser')

articles = soup.find_all ('article', class_='css-8atqhb')
data = []



with open ('nytimes.csv', 'w', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = ['title','description'])
    writer.writeheader()
    writer.writerows (data)

    for article in articles [:10]:
        title = article.find ('h2', class_='css-1vvhd4r').text.strip()
        description = article.find ('p', class_='css-1echdzn').text.strip()
        data.append ({'title':title,'description': description})
   

    print (soup)
