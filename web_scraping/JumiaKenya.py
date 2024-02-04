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

url = "https://www.jumia.co.ke/smartphones/"

response = requests.get (url)

soup = BeautifulSoup (response.content, 'html.parser')

product = soup.find_all ('span', class_= "text")
price = soup.find_all ('div',class_= "prc")
product_rating = soup.find_all ('h2', class_= "-m -upp -fs14 -pvs")


#for products in product:
    #print (product)

#for prices in price:
    #print (price)

for product_ratings in product_rating:
    print (product_rating)

#for brands in brand:
    #print (brand.text)

with open ("jumia.csv", 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerow (product_rating)




