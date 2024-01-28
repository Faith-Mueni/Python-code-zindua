"""
i) Product Name
ii) Brand Name
iii) Price (Ksh)
iv) Discount if Available (%)
v) Total Number of Reviews
vi) Product Rating (out of 5).
"""

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.jumia.co.ke/"

response = requests.get (url)

soup = BeautifulSoup (response.content, 'html.parser')

product = soup.find_all ('span', class_= "text")

data = []


with open ('jumia.csv', 'w', newline = '') as file:
        fields = ['product']
        writer = csv.DictWriter(file, fieldnames = fields)
        writer.writeheader()
        writer.writerows (data)

for products in product:
        product = product.find ('span', class_='text').text.strip()
        data.append ('fields')
