import requests
from bs4 import BeautifulSoup
import re


url = "https://zinduaschool.com"

response = requests.get(url)

#print (response.text)

soup = BeautifulSoup(response.content, 'html.parser')

urls_pattern = r"https[s]?://[?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*\\](\\),|(?:[0-9A-fA-])"
urls = re.findall (urls_pattern, response.text)

for url in urls:
    print (url)