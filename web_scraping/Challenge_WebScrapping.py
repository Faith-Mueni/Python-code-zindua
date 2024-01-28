#Use regular expression patterns to get phone  numbers, emails, and hyperlinks from the newyork times website

import requests
from bs4 import BeautifulSoup
import re

url = "https://www.nytimes.com"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{0-9}+$"

#emails = re.findall (email.pattern, response.content)
    
#print (emails)

#url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]"

#urls = re.findall (url_pattern, response.content)

#for url in urls:

    #print (url)

regex = r"(https?://\S+)"

hyperlinks = re.findall (regex,response.text)

for hyperlink in hyperlinks:

    print (hyperlink)